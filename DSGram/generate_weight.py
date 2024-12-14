import os
from openai import AzureOpenAI
import json
import numpy as np

# Initialize Azure OpenAI client with necessary credentials
client = AzureOpenAI(
    api_key="",
    api_version="",
    azure_endpoint=""
)

# Initialize lists to store text content and file names
txts = []
names = []

# Function to walk through a directory and gather text file contents and names
def walk(folder_path):
    # os.walk generates the file names in a directory tree
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Get the full file path
            full_path = os.path.join(root, file)
            # Append the file name to the 'names' list
            names.append(full_path.split('\\')[1])
            print(full_path.split('\\')[1])
            # Read the content of the file and append it to 'txts' list
            txts.append(open(full_path, 'r', encoding='utf-8').readlines())

# Define the folder path to search for text files
folder_path = 'data'
# Execute the walk function to populate 'txts' and 'names' lists
walk(folder_path)

# Function to make an API call to OpenAI with a given prompt
def make_api_call(prompt, system="", stop=None):
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0.60,
        model="gpt-4",
        max_tokens=512
    )
    # Extract the generated content from the API response
    ss = completion.choices[0].message.content
    ss = ss.replace('\\n', '\n')
    return ss

# Initialize an index for tracking iterations
idx = 0

# Read the system prompt from a file
pmt = open('./generate_weight_prompt.txt', "r", encoding='utf-8')
p = pmt.read()
print(p)

# Function to check the consistency of the generated JSON matrix
def check(json_data):
    # Convert JSON string to dictionary
    data_dict = json.loads(json_data)
    
    # Transform the dictionary to a numpy array
    matrix = np.array(list(data_dict.values()))
    
    # Calculate the principal eigenvalue and eigenvector
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    max_eigenvalue = np.max(np.real(eigenvalues))
    
    # Calculate the Consistency Index (CI)
    n = matrix.shape[0]
    CI = (max_eigenvalue - n) / (n - 1)
    
    # Random Index (RI) values for matrices from 1 to 10
    RI = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49]
    
    # Calculate the Consistency Ratio (CR)
    if n <= 10:
        CR = CI / RI[n]
    else:
        # Approximation for larger matrices
        CR = CI / (1.98 * (n - 2) / n)
    
    # Return 1 if CR < 0.1, otherwise 0
    return 1 if CR < 0.1 else 0

# List to store results
re = []

# Iterate through text content and file names
for x, name in zip(txts, names):
    prompts = []
    # Open and read the 'INPUT.txt' file
    fori = open("INPUT.txt", "r", encoding='utf-8')
    orilines = fori.readlines()
    
    # Create prompts by combining the original and corrected sentences
    for line, ori in zip(x, orilines):
        prompt = "original sentence: " + line + "corrected sentence: " + ori + '\n'
        prompts.append((p, prompt))
    
    ss = ""
    # Generate and save the inference results
    for sys, prompt in prompts:
        idx += 1
        print(idx)
        generated_text = ""
        lan = 5
        while True:
            try:
                # Call the API to generate a response
                generated_text = make_api_call(prompt, system=sys)
                print(generated_text)
                # Check if the generated text passes the consistency check
                while not check(generated_text) and lan:
                    print("redo", 5 - lan + 1)
                    generated_text = make_api_call(prompt, system=sys)
                    print(generated_text)
                    lan -= 1
                # If consistency check fails repeatedly, use a default value
                if not lan:
                    generated_text = """{
                    "Semantic Coherence":[1,1,1],
                    "Edit Level":[1,1,1],
                    "Fluency":[1,1,1]
                    }"""
                break
            except KeyboardInterrupt: 
                exit(0)
            except:
                print("wang redo ", 5 - lan + 1)
                lan -= 1
                if lan < 0:
                    # If an error occurs too many times, use a default value
                    generated_text = """{
                    "Semantic Coherence":[1,1,1],
                    "Edit Level":[1,1,1],
                    "Fluency":[1,1,1]
                    }"""
                    break
        
        # Accumulate the generated content
        ss += generated_text
        ss += '\n'
    
    # Save the accumulated content to a file
    f = open("./weight_SEEDA" + name + ".json", "w", encoding='utf-8')
    f.write(ss)
