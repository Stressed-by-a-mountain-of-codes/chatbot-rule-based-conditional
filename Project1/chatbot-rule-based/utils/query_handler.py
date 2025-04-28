from utils.file_reader import pick_random_line  # Importing the function
from utils.data_formatter import clean_input  # Importing the clean_input function

def process_query(user_input):
    """
    Processes the user input and returns an appropriate chatbot response.
    """
    user_input = clean_input(user_input)  # Clean the input for consistency

    # Handle greetings
    if any(word in user_input for word in ["hello", "hi", "hey", "good morning", "good evening", "howdy"]):
        return pick_random_line("data/greetings.txt")

    # Handle jokes
    elif any(phrase in user_input for phrase in ["joke", "make me laugh", "tell me a joke", "funny", "laugh"]):
        return pick_random_line("data/jokes.txt")

    # Handle motivation
    elif any(phrase in user_input for phrase in ["motivate", "inspire", "boost", "confidence", "feeling low", "give me strength"]):
        return pick_random_line("data/motivational_quotes.txt")

    # Handle study tips
    elif any(phrase in user_input for phrase in ["study", "exam", "tips", "learn", "revision"]):
        return pick_random_line("data/study_tips.txt")

    # Handle knowledge questions
    elif any(phrase in user_input for phrase in ["capital", "planet", "earth", "boil", "orbit", "python", "india", "largest planet", "longest river"]):
        return pick_random_line("data/knowledge_base.txt")

    # Handle weather
    elif any(phrase in user_input for phrase in ["weather", "rain", "sunny", "cold", "forecast"]):
        return pick_random_line("data/weather_data.txt")

    # Handle time and date
    elif any(phrase in user_input for phrase in ["time", "date", "current time", "current date", "what's the time", "what's the date"]):
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%B %d, %Y")
        responses = [
            f"The current time is: {current_time}. Hope you’re having a great day so far!",
            f"Today’s date is: {current_date}. Time flies, doesn't it?",
            f"It’s currently {current_time}. What are you up to at this time of the day?",
            f"The date today is {current_date}. It feels like the perfect time for a fresh start!",
            f"The time is now {current_time}. What are your plans for the rest of the day?",
            f"It’s {current_time} right now. Is it morning or evening for you where you are?",
            f"The date today is {current_date}. A great day to make the most of!",
            f"Currently, it's {current_time}. Let me know if you need any time-sensitive help!"
        ]
        import random
        return random.choice(responses)

    # Handle small talk
    elif any(phrase in user_input for phrase in ["how are you", "what's up", "how's it going", "how do you do", "how's everything"]):
        return pick_random_line("data/small_talk.txt")

    # Handle compliments
    elif any(phrase in user_input for phrase in ["you are great", "you are smart", "thank you", "thanks", "you rock"]):
        return pick_random_line("data/compliments.txt")

    # Handle facts
    elif "fact" in user_input:
        return pick_random_line("data/random_facts.txt")

    # Handle life advice
    elif any(phrase in user_input for phrase in ["life advice", "career advice", "life tips", "guidance", "help in life"]):
        return pick_random_line("data/life_advice.txt")

    # Handle tech trends
    elif any(phrase in user_input for phrase in ["technology", "tech", "latest technology", "new tech", "AI trends"]):
        return pick_random_line("data/tech_trends.txt")

    # Handle health tips
    elif any(phrase in user_input for phrase in ["health", "fitness", "exercise", "wellness", "mental health"]):
        return pick_random_line("data/health_tips.txt")

    # Handle books
    elif any(phrase in user_input for phrase in ["book", "recommend a book", "suggest a book", "reading suggestions"]):
        return pick_random_line("data/book_recommendations.txt")

    # Handle news
    elif "news" in user_input:
        return pick_random_line("data/news_summary.txt")

    # Handle current events
    elif any(phrase in user_input for phrase in ["current event", "world event", "latest news", "global event"]):
        return pick_random_line("data/current_events.txt")

    # If nothing matches, fallback
    else:
        return pick_random_line("data/fallback_responses.txt")
