import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


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
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'what is' in command:
        Article = command.replace('what is', '')
        info = wikipedia.summary(Article, 2)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    #elif 'crush' in command:
        #talk('Yes I have Crush on Rashmi')

    elif 'rashmi' in command:
        talk('Yes, Rashmi is twenty four years old beautiful girl. Rashmi has studied a radiotherapy technician course at the University of Swami Rama Himalayan. Rashmi is hardworking, generous and she has kind feelings. Rashmi is a beautiful girl with a beautiful soul, too. She is not envious, she is honest, and she truly loves people. Currently, she is falling in love with someone. Rashmi can laugh at anything, including herself. Rashmi is a gorgeous, humble and pure hearted person but no one takes her seriously. Rashmi is a beautiful girl in all aspects.')

    
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')


while True:
    run_alexa()