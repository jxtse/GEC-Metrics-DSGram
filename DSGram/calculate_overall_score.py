import json 
import os
import numpy as np

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
            names.append(full_path.split('\\')[1].split('.txt')[0])
            print(full_path.split('\\')[1])
            # Read the content of the file and append it to 'txts' list
            txts.append(open(full_path, 'r', encoding='utf-8').readlines())

# Define the folder path to search for text files
folder_path = 'data'
# Execute the walk function to populate 'txts' and 'names' lists
walk(folder_path)

# Function to calculate weighted score based on the principal eigenvector
def cal(score, weight):
    # Convert weight (sub-scores) into a numpy array (weights matrix)
    weights_matrix = np.array(list(weight.values()))

    # Extract the individual ratings from score (overall score)
    score_parts = score['output'].split(", overall")[0].split(',')
    ratings = {part.split(':')[0].strip(): float(part.split(':')[1].strip()) for part in score_parts}

    # Calculate eigenvalues and eigenvectors of the weights matrix
    eigenvalues, eigenvectors = np.linalg.eig(weights_matrix)
    # Find the principal eigenvector corresponding to the maximum eigenvalue
    max_eigen_index = np.argmax(eigenvalues)
    principal_eigenvector = np.real(eigenvectors[:, max_eigen_index])

    # Normalize the principal eigenvector to get the final weights
    weights = principal_eigenvector / np.sum(principal_eigenvector)
    
    print(weights)
    # Calculate the weighted score using the normalized weights and individual ratings
    weighted_score = np.dot(weights, [ratings['semantic coherence'], ratings['edit level'], ratings['fluency']])
    return weighted_score

# Iterate through each name (file) to calculate and save the final scores
for name in names:
    # Open and read the score and weight JSON files for each name
    scores = open("score_SEEDA" + name + ".json", 'r', encoding='utf-8')
    weights = open("weight_SEEDA" + name + ".json", 'r', encoding='utf-8')
    scores = scores.read()
    weights = weights.read()
    
    # Load the JSON content into dictionaries
    scores = json.loads(scores)
    weights = json.loads(weights)
    
    ss = ""
    idx = 0
    
    # Calculate the final weighted score for each pair of score and weight
    for score, weight in zip(scores, weights):
        fen = cal(score, weight)
        ss += fen
        idx += 1
        fen = str(fen)
        ss += fen + '\n'
    
    # Save the final scores into a text file with the same name
    f = open(name + ".txt", "w", encoding="utf-8")
    f.write(ss)
