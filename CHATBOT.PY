import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses
pairs = [
    [
        r"hi|hello|hey", 
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you?", 
        ["I'm good, thanks for asking!", "Doing great! How about you?"]
    ],
    [
        r"what is your name?", 
        ["I'm a chatbot created to chat with you!", "Call me ChatBot!"]
    ],
    [
        r"bye|goodbye", 
        ["Goodbye! Have a great day!", "Bye! See you soon!"]
    ],
    [
        r"(.*)", 
        ["That's interesting! Tell me more.", "I see. What else can you share?"]
    ]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    """
    Starts the chatbot interaction with the user.
    """
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    while True:
        try:
            user_input = input("You: ").strip()  # Get user input and remove extra spaces
            if user_input.lower() == 'bye':  # Check for exit condition
                confirm_exit = input("Are you sure you want to exit? (yes/no): ").strip().lower()
                if confirm_exit in ['yes', 'y']:
                    print("ChatBot: Goodbye! Have a nice day!")
                    break
                else:
                    print("ChatBot: Alright, let's continue!")
                    continue
            response = chatbot.respond(user_input)  # Generate chatbot response
            if response:
                print("ChatBot:", response)
            else:
                print("ChatBot: Sorry, I didn't understand that. Can you rephrase?")
        except Exception as e:
            print("ChatBot: Oops! Something went wrong. Please try again.")
            print(f"Error: {e}")  # Log the error for debugging

if __name__ == "__main__":
    start_chat()
