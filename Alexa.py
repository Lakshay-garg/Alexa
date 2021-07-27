import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def talk_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if "alexa" in command:
                command = command.replace("alexa", "")
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = talk_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is " + time)

    elif "who the heck is" in command:
        person = command.replace("who the heck is ", "")
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "date" in command:
        talk("sorry, I have an headache")
    elif "are you single" in command:
        talk("No, i m in relationship with Wifi")
    elif "joke" in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        talk("Please say the command again.")

while True:
    run_alexa()