def chatbot():
    print(" Chatbot: Hello! Type 'bye' to end the chat.")

    while True:
        user = input("You: ").lower()

        if user == "hi":
            print(" Chatbot: Hi!")
        elif user == "how are u":
            print(" Chatbot: I'm fine, thanks!")
        elif user == "bye":
            print(" Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")
chatbot()