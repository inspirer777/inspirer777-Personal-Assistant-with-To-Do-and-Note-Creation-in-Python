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
 1. Create a Note:
- You can dictate a note and it will be saved to a file.
 2. Add a To-Do:
- You can add tasks like "Buy groceries" to your to-do list.
3. View To-Do List:
- The assistant will read out all tasks in your to-do list.
4. Exit the Assistant:
- Saying "exit" will shut down the assistant.
Sample Code Snippet:
```py
import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()
speaker = pyttsx3.init()
speaker.setProperty('rate', 150)

todo_list = ['9 AM: wake up', '9:30 AM: eat breakfast', '10 AM: go to work']

def hello():
    speaker.say("Hello, how are you today?")
    speaker.runAndWait()

def create_note():
    speaker.say("What would you like to write on your note?")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio).lower()

                speaker.say("Choose a file name.")
                speaker.runAndWait()

                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio).lower()

            with open(f"{filename}.txt", 'w') as file:
                file.write(note)
                speaker.say(f"Successfully saved note in {filename}")
                speaker.runAndWait()
                done = True
        except speech_recognition.UnknownValueError:
            speaker.say("I did not understand, please try again.")
            speaker.runAndWait()

```
Starting the Assistant:
Run the assistant using the following code:
```py
from neuralintents import GenericAssistant

mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit": quit
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
assistant.train_model()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio).lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        speaker.say("I could not hear you, please try again.")
        speaker.runAndWait()

```
# Installation
Clone the repository:
```bash 
git clone https://github.com/yourusername/PersonalAssistant.git
cd PersonalAssistant

```
Install the required dependencies:
```bash
pip install speechrecognition pyttsx3 neuralintents

```
Run the assistant.py script:
```bash
python assistant.py

```
# License
This project is licensed under the MIT License - see the LICENSE file for details.

Authot :  back end 
# Good luck . 



