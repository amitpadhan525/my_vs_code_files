import random
import string
from nltk.stem import WordNetLemmatizer

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Intent dictionary
intents = {
    "greeting": ["hi", "hello", "hey", "good morning", "good evening"],
    "goodbye": ["bye", "see you", "goodbye", "take care"],
    "thanks": ["thanks", "thank you", "appreciate it"],
    "name": ["what is your name", "who are you"],
    "help": ["help", "can you help me", "i need assistance"]
}

# Response dictionary
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "Take care!", "See you soon!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "name": ["I'm CodBot, your internship assistant!"],
    "help": ["Sure! I'm here to help. Ask me anything."]
}

# Preprocessing function (uses basic split to avoid nltk.word_tokenize errors)
def preprocess(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return [lemmatizer.lemmatize(word) for word in tokens]

# Match user intent
def get_intent(user_input):
    processed = preprocess(user_input)
    for intent, keywords in intents.items():
        for word in processed:
            if word in [lemmatizer.lemmatize(k.lower()) for k in keywords]:
                return intent
    return None

# Main chat function
def chat():
    print("🤖 CodBot: Hello! I'm your chatbot. Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("🤖 CodBot: Goodbye!")
            break

        intent = get_intent(user_input)
        if intent:
            print(f"🤖 CodBot: {random.choice(responses[intent])}")
        else:
            print("🤖 CodBot: Sorry, I didn't understand that.")

# Run chatbot
if __name__ == "__main__":
    chat()
