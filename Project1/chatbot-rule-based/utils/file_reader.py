import random
import os

# Define the root path where the data folder is located
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))  # Get the current script directory

# Adjust the root path to the project root, which is one directory up
PROJECT_ROOT_PATH = os.path.dirname(ROOT_PATH)  # This will point to 'chatbot-rule-based'

# Global variable for controlling debug output
DEBUG_MODE = False  # Change this to True for debugging

def read_lines_from_file(file_path):
    """
    Reads all non-empty lines from a file and returns them as a list.
    """
    # Construct the full path to the file inside the 'data' folder
    full_path = os.path.join(PROJECT_ROOT_PATH, file_path)  # Use PROJECT_ROOT_PATH for data folder
    
    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"Error: {full_path} not found.")  # Debugging line to check for missing files
        return ["Oops! I couldn't find the information you're looking for."]

def pick_random_line(file_path):
    """
    Picks and returns a random line from a file.
    """
    lines = read_lines_from_file(file_path)
    
    # Debugging: Show the picked line only if DEBUG_MODE is True
    if DEBUG_MODE and lines:
        print(f"Picked random line from {file_path}: {lines[0]}")
    
    return random.choice(lines) if lines else "Sorry, I have nothing to say right now."
