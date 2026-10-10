def chatbot():
    print("🤖 Chatbot: Hello! I am a simple Python chatbot.")
    print("🤖 Chatbot: You can say 'hello', 'how are you', or 'bye'.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi! Nice to meet you!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How are you?")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


# Start the chatbot
chatbot()