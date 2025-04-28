import random

def pick_random_response(responses):
    """
    Picks and returns a random response from a given list.
    """
    if not responses:
        return "I'm not sure what to say!"
    return random.choice(responses)

def pick_best_match_response(responses, user_input):
    """
    (Optional) Picks a response that contains a keyword matching the user input.
    Falls back to random if no better match is found.
    """
    matches = [resp for resp in responses if any(word in resp.lower() for word in user_input.lower().split())]
    if matches:
        return random.choice(matches)
    else:
        return pick_random_response(responses)
