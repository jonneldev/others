import os
import re
from collections import Counter

# Directory to scan (replace with your directory path)
directory = r'C:\Users\Jonnel Dosado\OneDrive\Desktop\Projects\sample_folder'

# Regular expression pattern to match text inside parentheses
pattern = re.compile(r'\((.*?)\)')

# Function to extract the text inside parentheses from a filename
def extract_parentheses(filename):
    match = pattern.search(filename)  # Search for pattern in filename
    return match.group(1) if match else None  # Return text inside parentheses or None if not found

# List to store extracted strings from parentheses
parentheses_content = []

# Debugging print to check directory
print(f"Scanning directory: {directory}")

# Scan the directory and collect text inside parentheses
found_files = False
for root, _, files in os.walk(directory):
    for file in files:
        # Debugging print to check each file being processed
        print(f"Processing file: {file}")
        
        content = extract_parentheses(file)  # Extract text inside parentheses from each file
        if content:
            parentheses_content.append(content)  # Add extracted content to the list
            found_files = True  # Flag to indicate that files were found

# Check if any files were found
if not found_files:
    print(f"No files found in directory: {directory}")
else:
    # Debugging print to check extracted content
    print(f"Extracted content: {parentheses_content}")

    # Count occurrences of each extracted string
    counter = Counter(parentheses_content)

    # Identify and print substrings that occur more than once
    duplicates = {content: count for content, count in counter.items() if count > 2}
    print("Duplicate substrings inside parentheses (occurring more than once):")
    for content, count in duplicates.items():
        print(f'"{content}" occurs {count} times')

    # Optional: List files for each duplicate
    list_files = True  # Set to False if you don't want to list files
    if list_files:
        for content in duplicates:
            print(f'\nFiles containing "{content}":')
            for root, _, files in os.walk(directory):
                for file in files:
                    if content in file:
                        print(os.path.join(root, file))

print("Processing complete.")
