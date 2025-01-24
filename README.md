# Personal Assistant with To-Do and Note Creation in Python

This Python-based personal assistant allows users to create notes, manage a to-do list, and interact with the system using voice commands. Built using libraries like `speech_recognition`, `pyttsx3`, and `neuralintents`, it provides a voice-based interface to handle daily tasks.

## Features

- **Voice Interaction**: Uses speech recognition to listen and respond to voice commands.
- **Create Notes**: Allows users to dictate notes that are saved to files.
- **To-Do List**: Users can add tasks to a to-do list and review them later.
- **Greeting**: The assistant greets the user and checks on their well-being.
- **Exit Command**: Provides an exit command to shut down the assistant.
- **Text-to-Speech**: The assistant responds to the user via text-to-speech using `pyttsx3`.

## Requirements

- Python 3.x
- Required libraries: `speech_recognition`, `pyttsx3`, `neuralintents`

To install the required libraries, use `pip`:

```bash
pip install speechrecognition pyttsx3 neuralintents
```
How It Works
This assistant listens for user commands and performs actions based on predefined intents (like creating notes, adding tasks, etc.). Below are the main components of the code.

Key Functions:
hello(): Greets the user and asks how they're doing.
create_note(): Allows the user to dictate a note and saves it to a file.
add_todo(): Lets the user add items to their to-do list.
show_todos(): Reads out all the tasks in the to-do list.
quit(): Ends the assistant session.
Assistant Mappings:
The assistant listens to voice commands and maps them to functions as follows:
```py
mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit": quit
}
```
Example Usage:
- Create a Note:
- You can dictate a note and it will be saved to a file.
- Add a To-Do:
- You can add tasks like "Buy groceries" to your to-do list.
- View To-Do List:
- The assistant will read out all tasks in your to-do list.
Exit the Assistant:
- Saying "exit" will shut down the assistant.
Sample Code Snippet:

