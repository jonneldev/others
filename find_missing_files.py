import os
import pandas as pd
import re

# Function to extract the identifier (like A1, A2, etc.) from a filename
def extract_identifier(filename):
    if not isinstance(filename, str):
        return None  # Return None for non-string values
    match = re.search(r'\(([^)]+)\)', filename)  # Capture non-parenthesis characters
    return match.group(1) if match else None

# Define paths (replace with yours)
directory_to_check = r'C:\Users\Jonnel Dosado\OneDrive\Desktop\Projects\47'
excel_file = r'C:\Users\Jonnel Dosado\OneDrive\Desktop\Projects\sample.xlsx'

# Load Excel file with error handling
try:
    df = pd.read_excel(excel_file, header=None, usecols='A', skiprows=1)
except FileNotFoundError:
    print(f"Error: The file '{excel_file}' was not found.")
    exit()

# Function to find identifiers in filenames in the directory
def find_identifiers_in_directory(directory):
    identifiers = set()
    for root, _, files in os.walk(directory):
        for file in files:
            try:
                identifier = extract_identifier(file)
                if identifier:
                    identifiers.add(identifier)
            except Exception as e:
                print(f"Error processing file '{file}': {e}")
    return identifiers

# Find all identifiers in the directory
found_identifiers = find_identifiers_in_directory(directory_to_check)

# Convert DataFrame values to a list of strings
excel_filenames = df[0].astype(str).tolist()

# Find missing identifiers that are in Excel but not in the directory
missing_identifiers = [identifier for identifier in excel_filenames if identifier not in found_identifiers]

# Print results
if missing_identifiers:
    print("Missing identifiers (from Excel):")
    for identifier in missing_identifiers:
        print(f"- {identifier}")
else:
    print("All identifiers from Excel were found in directory.")

print("\nFile check complete.")
