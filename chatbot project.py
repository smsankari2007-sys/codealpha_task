print("🤖 Welcome to My Chatbot!")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user = input("You: ").lower().strip()

    # Greeting
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! 😊 How can I help you?")

    # How are you
    elif "how are you" in user or "you fine" in user:
        print("Bot: I'm fine! 😊 Thank you for asking.")

    # Name
    elif "your name" in user or "who are you" in user:
        print("Bot: My name is SimpleBot 🤖")

    # Weather
    elif "weather" in user or "temperature" in user:
        print("Bot: I can help with weather information! 🌤️")

    # Python
    elif "python" in user:
        print("Bot: Python is a popular programming language. 🐍")

    # Thanks
    elif "thank" in user or "thanks" in user:
        print("Bot: You're welcome! 😊")

    # Exit
    elif user == "bye" or user == "exit":
        print("Bot: Goodbye! Have a nice day! 👋")
        break

    # Unknown question
    else:
        print("Bot: Sorry, I don't understand that yet. 😅")
