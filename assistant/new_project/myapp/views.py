# myapp/views.py
import datetime
import pyjokes
import pywhatkit
from django.shortcuts import render
from django.http import JsonResponse
import speech_recognition as sr
import pyttsx3
import webbrowser
from .models import Destination


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
            response_data = {'text': "I couldn't understand you"}

        return JsonResponse(response_data)


def process_query(query):
    if 'open YouTube' in query:
        webbrowser.open('https://www.youtube.com/')
        speak("Opening YouTube.")
    elif 'play' in query:
        song = query.replace('play', '')
        pywhatkit.playonyt(song)
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
    elif 'home' in query:
        speak('abc')
    else:
        return "I'm sorry, I don't understand that command."


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
