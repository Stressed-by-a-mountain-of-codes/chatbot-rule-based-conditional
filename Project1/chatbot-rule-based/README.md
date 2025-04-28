Rule-Based Chatbot
This is a simple rule-based chatbot that uses conditional statements to generate responses based on user input. The chatbot provides responses based on predefined keywords, ensuring a consistent interaction with the user.

Features:
Conditional logic to handle various user queries (e.g., greetings, weather, current events, etc.).

Customizable responses stored in text files located in the data/ folder.

Clean code structure, with separated utility functions for managing different aspects of the chatbot's functionality.

File Structure:

chatbot-rule-based/
├── data/                       # Contains text files with various responses
│   ├── jokes.txt
│   ├── greetings.txt
│   ├── motivational_quotes.txt
│   ├── fallback_responses.txt
│   ├── weather_data.txt
│   ├── current_events.txt
│   └── ... (more data files)
├── utils/                       # Utility functions for the chatbot
│   ├── query_handler.py         # Handles input processing and response generation
│   ├── logger.py                # Logs chatbot interactions
│   ├── data_formatter.py        # Cleans and formats user input
│   └── file_reader.py           # Reads data files and picks random lines
├── main.py                      # Main entry point to run the chatbot
└── README.md                    # Project documentation
Getting Started:
Clone the repository to your local machine:

git clone <repository_url>
Navigate to the project directory:

cd chatbot-rule-based
Run the chatbot:

python main.py
Interact with the chatbot:

Enter commands like hello, weather, current events, etc.

Type exit or quit to stop the chatbot.

Functionality:
The chatbot responds based on specific keywords, which are matched through conditional checks in the process_query function. The chatbot has the following features:

Greeting responses: Responds to greetings like "hello", "hi", "hey", etc.

Weather information: Provides responses related to weather conditions.

Current events: Shares information about major events around the world.

Fallback responses: Provides a default message when the chatbot doesn't understand the user's query.

Customization:
Add or modify responses in the text files located inside the data/ folder.

You can add new conditions and responses in the process_query function to extend the chatbot's capabilities.

Example:
User: hello
Bot: Hey, how can I assist you today?

User: what's the weather like?
Bot: The skies are a bit overcast right now.