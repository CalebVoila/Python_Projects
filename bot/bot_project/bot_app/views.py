from django.shortcuts import render
from django.http import HttpResponse
import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from pyjokes import pyjokes

# Create your views here.

def index(request):
    return render(request, 'bot.html')

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
activationword= 'computer'

def speak(text, rate= 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()


def command():
    listner=sr.Recognizer()
    print('listening for a command')

    with sr.Microphone() as source:
        listner.pause_threshold=2
        input_speech=listner.listen(source)

    try:
        print('Recognizing speech......')
        query=listner.recognize_google(input_speech,language='en_gb')
        print(f'the input speech was: {query}')
    except Exception as exception:
        print('I didnt get you')
        speak('I didnt get you')

        print(exception)
        return 'None'

    return query

def main(request):
     speak("all systems nomial.")
     while True:
          query = command().lower()
          print(query)
          if 'hello' in query:
            speak('hello karthik')
          elif 'play' in query:
             song = query.replace('play', '')
             speak('playing' + song)
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


