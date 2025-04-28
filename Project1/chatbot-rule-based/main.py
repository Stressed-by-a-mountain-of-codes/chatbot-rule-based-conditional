import sys
import time
from utils.query_handler import process_query
from utils.logger import log_message
from utils.data_formatter import clean_input

def slow_type(text, delay=0.02):
    """
    Types out the text slowly like a human for better user experience.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to next line

def show_thinking_dots(message="Thinking", dots=3, delay=0.5):
    """
    Shows a loading animation with dots.
    """
    sys.stdout.write(f"{message}")
    sys.stdout.flush()
    for _ in range(dots):
        time.sleep(delay)
        sys.stdout.write(".")
        sys.stdout.flush()
    print()  # Move to next line

def main():
    slow_type("🤖 Hello! I am your rule-based chatbot. How can I help you today?", delay=0.03)
    log_message("Chatbot started.", "INFO")
    
    while True:
        try:
            # Take user input
            user_input = input("You: ")

            # Clean the input (for consistency)
            cleaned_input = clean_input(user_input)

            # Exit condition
            if cleaned_input in ["exit", "quit", "bye"]:
                slow_type("Bot: Goodbye! Have a great day!", delay=0.03)
                log_message(f"Session ended by user input: {cleaned_input}", "INFO")
                break  # Exit the loop

            # Show thinking animation
            show_thinking_dots()

            # Process the query and get response
            response = process_query(user_input)

            # Output the response
            slow_type(f"Bot: {response}", delay=0.03)

            # Log the conversation
            log_message(f"User: {user_input} | Bot: {response}", "INFO")

        except KeyboardInterrupt:
            slow_type("\nBot: Session ended. See you next time!", delay=0.03)
            log_message("Session terminated with KeyboardInterrupt.", "INFO")
            break

        except Exception as e:
            slow_type("Bot: Oops! Something went wrong.", delay=0.03)
            log_message(f"Error: {str(e)}", "ERROR")

if __name__ == "__main__":
    main()
