import os

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
            # Extract the file name without extension and add it to 'names' list
            names.append(full_path.split('\\')[1].split(".txt")[0])
            # Print the file name
            print(full_path.split('\\')[1])
            # Read the content of the file and append it to 'txts' list
            txts.append(open(full_path, 'r', encoding='utf-8').readlines())

# Define the folder path to search for text files
folder_path = 'data'
# Execute the walk function to populate 'txts' and 'names' lists
walk(folder_path)
# Print the names of the text files
print(names)

# Open and read the content of the 'INPUT.txt' file
ori = open('INPUT.txt', 'r', encoding='utf-8')
ori = ori.readlines()

from openai import AzureOpenAI

# Initialize Azure OpenAI client with necessary credentials
client = AzureOpenAI(
    api_key="",
    api_version="",
    azure_endpoint=""
)

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
        temperature=0.6,
        model="gpt-4o",
        max_tokens=512
    )
    # Extract the generated content from the API response
    ss = completion.choices[0].message.content
    ss = ss.replace('\\n', '\n')
    return ss

# Read the system prompt from a file
pmt = open('./generate_score_prompt.txt', "r", encoding='utf-8')
p = pmt.read()
print(p)

# Iterate over the number of files to generate and score corrections
for _ in range(15):
    prompts = []
    tot = 0
    # Create prompts by combining the original and corrected sentences
    for i in range(len(ori)):
        prompt = "original sentence: " + ori[i] + ", corrected sentence: " + txts[_][i]
        prompts.append((p, prompt))
        tot = tot + 1
    print(tot)
    idx = 0
    ss = ""
    # Open a new file to save the results
    f = open("./score_SEEDA" + names[_] + ".json", "w", encoding='utf-8')
    
    # Generate and save the inference results
    for sys, prompt in prompts:
        idx = idx + 1
        print(idx)
        generated_text = ""
        while True:
            try:
                # Call the API to generate a response
                generated_text = make_api_call(prompt, system=sys)
                break
            except KeyboardInterrupt:
                exit(0)
            except:
                continue
        
        print(generated_text)
        ss += generated_text
        ss += '\n'
    
    # Write the generated content to the file
    f.write(ss)
