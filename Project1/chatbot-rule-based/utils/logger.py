import datetime

def log_message(message, log_type="INFO"):
    """
    Logs a message with a timestamp and a type (INFO, ERROR, etc.).
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_message = f"[{timestamp}] [{log_type}] {message}\n"
    
    try:
        with open("chatbot.log", "a", encoding="utf-8") as log_file:
            log_file.write(formatted_message)
    except Exception as e:
        print(f"Logging failed: {e}")
