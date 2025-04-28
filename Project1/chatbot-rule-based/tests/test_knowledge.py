import unittest
from utils.query_handler import process_query

class TestKnowledgeResponse(unittest.TestCase):
    def test_knowledge_queries(self):
        # List of knowledge-related user questions
        knowledge_queries = [
            "What is the capital of France?",
            "Tell me about Jupiter.",
            "How many days does the Earth take to orbit the Sun?",
            "At what temperature does water boil?",
            "Which is the largest planet?"
        ]
        
        for query in knowledge_queries:
            response = process_query(query)
            self.assertTrue(
                any(keyword in response.lower() for keyword in ["paris", "jupiter", "365", "100", "jupiter"]),
                msg=f"Failed for input: {query}"
            )

if __name__ == '__main__':
    unittest.main()
