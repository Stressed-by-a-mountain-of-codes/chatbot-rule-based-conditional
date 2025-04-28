import unittest
from utils.query_handler import process_query

class TestMotivationResponse(unittest.TestCase):
    def test_motivation_queries(self):
        # List of motivational or inspiring inputs
        motivation_inputs = [
            "I need motivation",
            "Inspire me",
            "Give me a motivational quote",
            "I feel low",
            "Boost my confidence"
        ]
        
        for user_input in motivation_inputs:
            response = process_query(user_input)
            self.assertTrue(
                any(word in response.lower() for word in ["you can", "believe", "achieve", "never give up", "success"]),
                msg=f"Failed for input: {user_input}"
            )

if __name__ == '__main__':
    unittest.main()
