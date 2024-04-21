# myapp/views.py
import datetime
import pyjokes

from django.shortcuts import render

import speech_recognition as sr
import pyttsx3
import webbrowser
from .models import Destination
from .models import Local_news


def index(request):
    # Query all Destination objects from the database
    dests = Destination.objects.all()
    return render(request, 'index1.html', {'dests': dests})


def voice_assistant(request):
    if request.method == 'POST':
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak('listening...!')
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}")
            response_text = process_query(query)
            response_data = {'text': response_text}
        except Exception as e:
            speak("Could not understand audio.")

    return render(request, 'index1.html')


def process_query(query):
    if 'open YouTube' in query:
        webbrowser.open('https:/www.youtube.com/')
        speak("Opening YouTube.")
    elif 'play' in query:
        song = query.replace('play', '')
        url = 'http://localhost:8000/play/'
        webbrowser.open(url)
        speak("Playing" + song)
    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M%p')
        speak("The current time is " + time)
    elif 'wish' in query:
        speak("Hello! How can I assist you today?")
    elif 'joke' in query:
        a = pyjokes.get_joke()
        print(a)
        speak(a)
    elif 'news' in query:
        url = 'http://localhost:8000/news/'
        webbrowser.open(url)
        speak('opening news')
    elif 'sports' in query:
        url = 'http://localhost:8000/sports/'
        webbrowser.open(url)
        speak('opening news')
    elif 'entertainment' in query:
        url = 'http://localhost:8000/entertainment/'
        webbrowser.open(url)
        speak('opening news')
    elif 'cartoon' in query:
        url = 'http://localhost:8000/cartoon/'
        webbrowser.open(url)
        speak('opening news')

    else:
        speak("I'm sorry, I don't understand that command.")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def after_joke(request):
    abcd = 'WLkkaBMU5EM'
    return render(request, 'play.html', {'source': abcd})


def news(request):
    objects = Local_news.objects.all()
    return render(request, 'news.html', {'objects': objects})
def sports(request):
    objects = Local_news.objects.all()
    return render(request, 'news.html', {'objects': objects})
def entertainment(request):
    objects = Local_news.objects.all()
    return render(request, 'news.html', {'objects': objects})
def cartoon(request):
    objects = Local_news.objects.all()
    return render(request, 'news.html', {'objects': objects})
