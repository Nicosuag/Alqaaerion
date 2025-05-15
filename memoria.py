# memoria.py - Simulating a safe with a key

import os

# Check if the required conda environment is activated
if "CONDA_DEFAULT_ENV" not in os.environ or os.environ["CONDA_DEFAULT_ENV"] != "uwpico":
    print("Warning: The 'uwpico' conda environment is not activated.")
    print("Please activate it using 'conda activate uwpico' before running this script.")
    exit()

safe_content = {
    "secret_number": 12345,
    "important_data": "This is sensitive information.",
    "random_numbers": [9, 8, 1, 1, 9, 8, 1, 1]
}

key = 9811

def unlock_safe(attempt):
    if attempt == key:
        return safe_content
    else:
        return "Incorrect key. Access denied."

# Example usage:
# print(unlock_safe(9811))
