import datetime
import winshell
from ecapture import ecapture as ec
import win32com.client as wincl
import subprocess
import wikipedia
import json
from urllib.request import urlopen
import speech_recognition as sr
import win32com.client
import webbrowser
import os
import pyjokes
from win32com.client import Dispatch
import distutils
import pyttsx3
import openai
from config import apikey
from config import password
import openai
import smtplib
import time
import requests
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        say("Good Morning  !")

    elif hour >= 12 and hour < 18:
        say("Good Afternoon  !")

    else:
        say("Good Evening  !")


    say("I am your Assistant")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()


    server.login('vishnukv2349@ieee.org', password)
    server.sendmail('your email id', to, content)
    server.close()
def username():
    say("What should i call you ")
    uname = takeCommand()
    say("Welcome Mister")
    say(uname)


    say("How can i Help you")

def ai(prompt):
    openai.api_key = apikey
    messages = [{"role": "system", "content": "You are a intelligent assistant."}]

    message = prompt
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
    return reply


#speaker= win32com.client.Dispatch("SAPI.SpVoice")

# todo: try to find ava like voice somwhere
def say(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            print("recognizing..")
            query=r.recognize_google(audio,language="en-in")
            print(f"User said:{query}")
            return query.lower()
        except Exception as e:
            print("Some Error Occured, Please say the Commands again")
if __name__ == '__main__':
    say("Hello I am AVA  ")
    wishme()
    username()
    while True:
        print("Listening...")
        query=takeCommand()
        sites=[["youtube","https://youtube.com"],["instagram","https://instagram.com"],["google","https://google.com"]]
        print("The text:",query)
        #say(query)
        if query:
            for site in sites:
                if f"open {site[0]}".lower() in query:
                    say(f"Opening {site[0]}")
                    webbrowser.open(site[1])
            if "the time" in query:
                strftime=datetime.datetime.now().strftime("%H:%M:%S")
                say(f"The time is {strftime}")
           # elif "using artificial intelligence" in query:
            #    ai(prompt=query)
            elif 'how are you' in query:
                say("I am fine, Thank you")
                say("How are you")
            elif 'joke' in query:
                say(pyjokes.get_joke())
            elif 'fine' in query or "good" in query:
                say("It's good to know that your fine")
            elif 'using wikipedia' in query.lower():
                say('Searching Wikipedia...')
                try:
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=3)
                    print(results)
                    say(results)
                except Exception as e:
                    print(e)
                    say("Sorry, I am not able to find anything")

            elif 'send a mail' in query:
                try:
                    print("What should I say?")
                    say("What should I say?")
                    content = takeCommand()
                    print("whom should i send")
                    say("whom should i send")
                    to = input()
                    sendEmail(to, content)
                    print("Email sent!!!")
                    say("Email has been sent !")
                except Exception as e:
                    print(e)
                    say("I am not able to send this email")
                    # todo: find how to give integer type inputs
            elif "don't listen" in query or "stop listening" in query:
                say("for how much time you want to stop jarvis from listening commands")
                a = int(takeCommand())
                print(a)
                time.sleep(a)
                print(a)
            elif 'open brave' in query:
                codePath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Brave.lnk"
                os.startfile(codePath)
            elif 'open music' in query:
                codePath = r"C:\Users\wishn\.idlerc\Downloads\upbeat-summer-pop-113447.mp3"
                os.startfile(codePath)
            elif 'open video' in query:
                codePath = r"C:\Users\wishn\.idlerc\Downloads\Rick Astley - Never Gonna Give You Up (Official Music Video).mp4"
                os.startfile(codePath)
            elif 'news' in query:

                try:
                    jsonObj = urlopen(
                        '''https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=81025fc3636f4097ad33b6dc5f87d87c''')
                    data = json.load(jsonObj)
                    i = 1

                    say('here are some top news from the times of india')
                    print('''=============== TIMES OF INDIA ============''' + "\n")

                    for item in data['articles']:
                        print(str(i) + '. ' + item['title'] + '\n')
                        print(item['description'] + '\n')
                        say(str(i) + '. ' + item['title'] + '\n')
                        i += 1

                except Exception as e:

                    print(str(e))
            elif 'exit' in query:
                say("Thanks for giving me your time")
                exit()
            elif 'joke' in query:
                say(pyjokes.get_joke())

            elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
                say("Recycle Bin Recycled")
            elif "camera" in query or "take a photo" in query:
                ec.capture(0, "Camera ", "img.jpg")



            elif "log off" in query or "sign out" in query:
                say("Make sure all the application are closed before sign-out")
                time.sleep(5)
                subprocess.call(["shutdown", "/l"])
            else:
                print("chatting")
                reply=ai(query)
                say(reply)

        else:
            print("query not recieved")


