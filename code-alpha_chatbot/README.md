# Basic Rule-Based Chatbot 🤖

## Project Overview
The Basic Rule-Based Chatbot is a simple Python program that interacts with users through predefined messages and responses. It checks the user's input and selects an appropriate reply based on predefined conditions.

For example, when the user types "hello", the chatbot responds with "Hi!".

## Features
- Recognizes basic messages such as "hello", "how are you", and "bye".
- Provides predefined responses to recognized messages.
- Uses conditional statements to select replies.
- Can continue the conversation using a loop.
- Can display a default response for unrecognized messages.
- Runs entirely in the console.

## Technologies Used
- Python 3
- Built-in Python functions and statements

## Sample Conversation

```text
Chatbot: Hello! Welcome to the chatbot.
You: hello
Chatbot: Hi!

You: how are you
Chatbot: I'm fine, thanks!

You: bye
Chatbot: Goodbye!
```

## Key Concepts
- If-elif-else statements
- Functions
- While loops
- User input and output
- String handling
- Basic conditional logic

## How to Run
1. Install Python 3 on your computer.
2. Save the code in a file named `chatbot.py`.
3. Open a terminal or command prompt in the project folder.
4. Run the following command:

```bash
python chatbot.py
```

## How It Works
1. The chatbot asks the user to enter a message.
2. It checks the input against predefined conditions.
3. It displays the corresponding response.
4. If the input is not recognized, it can display a default message.
5. The conversation continues until the user types an exit message, such as "bye", if an exit loop is implemented.

## Future Improvements
- Add more questions and responses.
- Make input case-insensitive.
- Recognize additional greetings and keywords.
- Add a conversation history.
- Integrate an AI API for more advanced conversations.

## Conclusion
This project introduces beginners to rule-based programming, functions, loops, and conditional statements by building a simple interactive chatbot.