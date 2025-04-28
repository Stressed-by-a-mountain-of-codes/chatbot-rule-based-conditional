import re

def clean_input(user_input):
    """
    Cleans the user input by:
    - Stripping leading/trailing spaces
    - Converting to lowercase
    - Removing extra spaces
    - Optionally removing special characters (like punctuation)
    """
    # Convert to lowercase and strip extra spaces
    cleaned = user_input.strip().lower()
    cleaned = ' '.join(cleaned.split())

    # Optionally, remove special characters (like punctuation)
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', cleaned)

    return cleaned

def format_response(response_text):
    """
    Formats the chatbot's response text if needed.
    Right now, just ensures it's clean and has proper spacing.
    """
    formatted = response_text.strip()
    # You could add more formatting rules here if necessary
    return formatted
