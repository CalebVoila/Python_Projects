from django.shortcuts import render
import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from pyjokes import pyjokes

# Initialize pyttsx3 engine and set properties
engine = None

def initialize_engine():
    global engine
    if engine is None:
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)

def speak(text, rate=120):
    """
    Function to speak the given text using pyttsx3 engine.
    """
    initialize_engine()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def command():
    """
    Function to recognize speech using speech_recognition library.
    """
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech...')
        query = listener.recognize_google(input_speech, language='en_gb')
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I didn\'t get you')
        speak('I didn\'t get you')
        print(exception)
        return 'None'

    return query

def main(request):
    if request.method == 'POST':
        speak("All systems nominal.")
        while True:
            query = command().lower()
            print(query)
            if 'hello' in query:
                speak('Hello karthik')
            elif 'play' in query:
                song = query.replace('play', '')
                speak('Playing ' + song)
                pywhatkit.playonyt(song)
            elif 'time' in query:
                time = datetime.datetime.now().strftime('%I:%M%p')
                speak("The current time is " + time)
            elif 'who is' in query:
                name = query.replace('who is', '')
                info = wikipedia.summary(name, 1)
                speak(info)
            elif 'joke' in query:
                speak(pyjokes.get_joke())
            elif 'thank' in query:
                break

    return render(request, 'bot.html')
