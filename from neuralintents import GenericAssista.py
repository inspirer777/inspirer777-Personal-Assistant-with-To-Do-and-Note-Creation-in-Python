from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3
import sys

recognizer= speech_recognition.Recognizer()

speaker = pyttsx3.init()
speaker.setProperty('rate',150)

todo_list=['9 Am : wake up ','at 9:30 eat breakfast','10 go work'
,'8 pm goback home ','8:30 PM take a shower and relax','11 Pm go to sleep']

def create_note():
    global recognizer

    speaker.say("what do you want to write onto your note")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("choose a file name ")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)

                filename=recognizer.recognize_google(audio)
                filename = filename.lower()
            with open(filename,'w') as f:
                f.write(note)
                done = True
                speaker.say("Sucseesfuly amir {filename}")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand you! plese try again")
            speaker.runAndWait()
def add_todo():
    global recognizer

    speaker.say("what todo do you want to add ?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done=True

                speaker.say("i did not understand. please try again!")
                speaker.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand. please try again!")
            speaker.runAndWait()

def show_todos():

    speaker.say("this is for you Amir Arab ")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def hello():
    speaker.say("hello  Amir how are you today ?")
    speaker.runAndWait()

def quit():
    speaker.say("Good bye amir   see you lator , take care")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo":add_todo,
    "show_todos":show_todos,
    "exit":quit


}


assitant = GenericAssistant('D:/python/vscode/ss.json',intent_methods=mappings)
assitant.train_model()
while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assitant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()

