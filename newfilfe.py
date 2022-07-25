from translate import Translator
import pyttsx3
import wolframalpha
import os
import subprocess
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime as dt
import shutil
import glob 
import re
import pyjokes as pj
import requests
import json
from chatbot import demo
import time 
 

a=int(input("""Input your assistain voice:
0.Male
1.Female: 
"""))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[a].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishme():
    hour = int(dt.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evenning")
    speak("I am nelexa 2 point o how may i help u")

def takeCommand():
	
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.7
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-ne')
        print(f"User said: {query}\n")
        
    except Exception as e:
        print(e)
        print("Unable to Recognize your voice....")
        return "None"
	
    return query

joke_talk = (pj.get_joke(language="en", category="neutral"))

if __name__ == "__main__":

    wishme()

    while True:
        query=takeCommand().lower()

        if 'play music'in query:
            music_dir="C:\\Users\\Admin\\hackathon"
            songs=os.listdir(music_dir)
            random = os.startfile(os.path.join(music_dir, songs[2]))

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open TikTok' in query:
            webbrowser.open("tiktok.com")
            
        elif 'open Instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open WhatsApp' in query:
            webbrowser.open("whatsapp.com")

        elif 'open GitHub' in query:
            webbrowser.open("github.com")

        elif 'stop' in query:
            os.system(exit())
            
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search'in query:
            speak('Searching for result...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            print(results)
            speak(results)

        elif 'shutdown' in query:
            j=input("Do you want to shutdown your computer?(yes/ no)")
            if j=="yes":
                os.system("shutdown /s /t 1")
            else:
                exit();

        elif 'restart' in query:
            y=input("Do you want to restart your computer?(yes/ no)")
            if y=="yes":
                os.system("shutdown /r /t 1")
            else:
                exit();

        elif 'sleep' in query:
            u=input("Do you want to hibernize your computer?(yes/ no)")
            if y=="yes":
                os.system("shutdown /h /t 1")
            else:
                exit();

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")

        elif 'open boston college webpage' in query:
            webbrowser.open("bostoncollege.edu.np")
        
        elif 'search' and 'music file' in query:
            os.chdir("/mydir")
            for file in glob.glob("*.mp3","*.ogg",):
                print(file)

        elif 'search' and 'python file' in query:
            os.chdir("/mydir")
            for file in glob.glob("*.py"):
                print(file)

        elif 'search' and 'video file' in query:
            os.chdir("/mydir")
            for file in glob.glob("*.mp4","*.mkv"):
                print(file)

        elif 'open' and 'image file' in query:
            os.chdir("/mydir")
            for file in glob.glob("*.jpg","*.png"):
                print(file)

        elif 'the time' in query:
            strTime = dt.datetime.now().strftime("%H:%M")
            speak(f"The time is:{strTime}")
            print(f"The time is:{strTime}")
        
        elif 'stop' in query:
            speak("Thanks for giving me your time")
            exit();

        elif 'joke' in query:
            speak(joke_talk)

        elif 'would you like to chat with me' in query:
            speak("yeah why not but this features is only available in typing mode")
            demo()
		
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop nelaxa from listening commands")
            g = int(takeCommand())
            time.sleep(g)
            print(g)

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by students of ncc")

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client("API_ID")
            res = client.query(query)

            try:
                print (next(res.results).text)
                speak (next(res.results).text)

            except StopIteration:
                print ("No results")
			
        elif "calculate" in query:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop Nelaxa from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif '' in query:
            speak("This function is not available in this version for another version click the link below")
            k= input("Do you want to redirect to the Nelexa 3.o website?(yes/ no)")
            if k=="yes":
                webbrowser.open("voice.capitalclubapi.repl.co")
            else:
                exit();
