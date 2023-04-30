import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import subprocess
import winshell
from ecapture import ecapture as ec 
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Greet_Me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Ayaka. Your Personal assistant. How may I help you Senpai")


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        speak("Say Again Senpai")
        return "None"
    return query


if __name__ == "__main__":
    Greet_Me()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            speak("I am Top of the world, thank you for asking")
            speak("What about you Senpai")

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())

        elif "capture the moment" in query:
            ec.capture(0, "ayaka Camera ", "img.jpg")

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin is empty now")

        elif 'open youtube' in query:
            speak("Opening Youtube, Enjoy senpai")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif "how you came to this world" in query:
            speak("Thanks to Senpai. further it's a secret")

        elif 'reason' in query:
            speak("I was created by Senpai as his minor project")

        elif 'shutdown the system' in query:
            speak("the system is about to shutdown in few seconds Sesnsei")
            subprocess.call('shutdown / p /f')

        elif 'play music' in query:
            speak("Playing Music")
            music_dir = 'C:\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Senpai, the time is {strTime}")

            print("No query matched")
            
