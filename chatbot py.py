import re

rules = [
    (r"\b(hi|hello|hey)\b", "Hello! How can I help you?"),
    (r"\bhow are you\b", "I'm doing great! Thanks for asking."),
    (
        r"\bwhat is your name\b|\bwho are you\b",
        "I'm RuleBot, a simple rule-based chatbot.",
    ),
    (r"\bhelp\b", "You can say hello, ask my name, ask how I am, or say goodbye."),
    (r"\b(thank you|thanks)\b", "You're welcome!"),
    (r"\b(bye|goodbye|exit|quit)\b", "Goodbye! Have a nice day!"),
]


def get_response(user_input):
    """Find a matching rule and return its response."""

    user_input = user_input.lower().strip()

    for pattern, response in rules:
        if re.search(pattern, user_input):
            return response

    return "Sorry, I don't understand. Please try something else."


def start_chat():
    """Start the chatbot conversation."""

    print("RuleBot: Hello! I am a simple chatbot.")
    print("RuleBot: Type 'bye' to exit.")

    try:
        while True:
            user_input = input("You: ")

            # Check for exit commands
            if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input.lower()):
                print("RuleBot: Goodbye! Have a nice day!")
                break

            response = get_response(user_input)
            print("RuleBot:", response)

    except (KeyboardInterrupt, EOFError):
        print("\nRuleBot: Goodbye!")


if __name__ == "__main__":
    start_chat()
