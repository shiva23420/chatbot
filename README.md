# chatbot
## Overview
This is a basic rule-based chatbot built using Python. It interacts with the user through the command line by responding to a few predefined messages.

## Features
- Greets the user.
- Responds to "hi".
- Answers "how are u".
- Ends the conversation when the user types "bye".
- Displays a default message for unknown inputs.

## Requirements
- Python 3.x

## How to Run

1. Save the Python code in a file named `chatbot.py`.
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command:

```bash
python chatbot.py
```

## Sample Output

```
Chatbot: Hello! Type 'bye' to end the chat.

You: hi
Chatbot: Hi!

You: how are u
Chatbot: I'm fine, thanks!

You: hello
Chatbot: Sorry, I don't understand that.

You: bye
Chatbot: Goodbye!
```

## Supported Commands

| User Input | Chatbot Response |
|------------|------------------|
| hi | Hi! |
| how are u | I'm fine, thanks! |
| bye | Goodbye! (Ends the program) |
| Any other input | Sorry, I don't understand that. |

## Project Structure

```
Simple-Chatbot/
│
├── chatbot.py
└── README.md
```

## How It Works

- The chatbot continuously waits for user input using a `while` loop.
- User input is converted to lowercase using `.lower()`.
- It checks the input using `if`, `elif`, and `else` statements.
- The conversation continues until the user enters `bye`.
