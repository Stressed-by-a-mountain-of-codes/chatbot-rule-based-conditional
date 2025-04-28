import unittest
from utils.query_handler import process_query

class TestGreetingResponse(unittest.TestCase):
    def test_greeting_input(self):
        # List of possible greetings the user might enter
        greetings = ["hello", "hi", "hey", "good morning", "good evening"]
        
        for greeting in greetings:
            response = process_query(greeting)
            self.assertTrue(
                any(word in response.lower() for word in ["hello", "hi", "greetings", "hey"]),
                msg=f"Failed for input: {greeting}"
            )

if __name__ == '__main__':
    unittest.main()
