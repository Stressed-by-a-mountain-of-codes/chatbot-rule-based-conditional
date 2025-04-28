import unittest
from utils.query_handler import process_query

class TestFallbackResponse(unittest.TestCase):
    def test_unknown_input(self):
        # Giving input that the bot won't recognize
        user_input = "blablabla something random"
        response = process_query(user_input)
        
        # We check if the fallback response is used
        self.assertIn("sorry", response.lower())  # or check a part of your fallback text
        
if __name__ == '__main__':
    unittest.main()
