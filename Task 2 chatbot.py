import nltk
from nltk.chat.util import Chat, reflections


pairs = [
    [
        r"hi|hello|hey", 
        ["Hello! How can I help you?", "Hi there! What can I do for you?"]
    ],
    [
        r"(.) your name(.)", 
        ["I am a simple chatbot created for this task."]
    ],
    [
        r"how are you", 
        ["I'm just a bot, but I'm functioning as expected!"]
    ],
    [
        r"bye|goodbye", 
        ["Goodbye! Have a great day!", "Bye! Take care!"]
    ]
]


chatbot = Chat(pairs, reflections)


print("Hello! I am a chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print(f"Chatbot: {response}")