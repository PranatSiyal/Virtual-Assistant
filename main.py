import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import pywhatkit
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
    except:
        pass
    return command


def run_Jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Yes Sir, playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Sir the Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print('Sir'+info)
        talk(info)
    elif 'what are you' in command:
        talk('your assistant, named after iron mans voice assistant')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'go' in command:
        pywhatkit.sendwhatmsg('+91 96534 12923', pyjokes.get_joke(), 12, 56)

    else:
        talk('Please say the command again.')


while True:
    run_Jarvis()