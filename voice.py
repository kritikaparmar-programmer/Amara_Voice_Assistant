import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyjokes
import subprocess
import shutil
import smtplib
import requests
from twilio.rest import Client
import time
import wolframalpha
import ecapture as ec


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    
    elif hour>=16 and hour<23:
        speak("Good evening!")

    else:
        speak("Good night!")
        
    speak("I am Amara, Your personal Voice Assistant")


def usrname():
    speak("What should i call you?")
    uname = takeCommand()
    speak("Welcome ")
    speak(uname)
    columns = shutil.get_terminal_size().columns 
    print("######################################################".center(columns))
    print("Welcome ", uname.center(columns))
    print("######################################################".center(columns))
    speak("How can i Help you?")


def takeCommand():
    '''
    takes microphone input from the user and returns 
    string output
    '''

    r = sr.Recognizer()  # helps in recognizing audio
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        speak("Pardon me, please say that again")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('your email id', 'your email passowrd')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    speak("Hey There!")
    wishMe()
    usrname()
    while(True):
        query = takeCommand().lower()

        # executing tasks logic
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            try:
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("I am not ablem to process your request right now. In what other way I can help you?")

        elif "open youtube" in query:
            webbrowser.open("http://www.youtube.com")
            speak("youtube is open now")

        elif "open google" in query:
            webbrowser.open("http://www.google.com")
            speak("Google chrome is open now")

        elif 'open gmail' in query:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")

        elif "open github" in query:
            webbrowser.open("http://www.github.com")
            speak("Github is open now")

        elif "play spotify playlist" in query:
            webbrowser.open("https://open.spotify.com/playlist/0j4JOCvBS255fd2B1Nwdj1?si=7rtrNfctTyu8Q9Hvlq0h9A")
            speak("Enjoy your fav playlist!")

        elif 'search' in query or 'who is' in query:
            query = query.replace("search", "")  
            query = query.replace("who is", "")          
            webbrowser.open_new_tab(query) 
            speak("Your request has processed")

        elif "what time" in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {Time}")
            speak(f"The time is {Time}")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"robo camera","img.jpg")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you?") 
            ui = takeCommand().lower()
            if "good" in ui:
                speak("That's great!")
                speak("Why you have called me?")
            elif "bad" in ui:
                speak("Oh! Ask me to tell you a joke or tell me what can I do for you?")
            else:
                speak("Ok! I'm guessing its good!")
        
        elif 'ask' in query:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id="Paste your unique ID here "
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "what's your name" in query or "what is your name" in query or "your name" in query:
            speak("My friends call me Amara")
            print("My friends call me Amara")  

        elif "who made you" in query or "who created you" in query: 
            speak("I have been created by Kritika Parmar")  

        elif 'joke' in query:
            speak(pyjokes.get_joke())   

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif "why you came to the world" in query:
            speak("Thanks to Kritika. By the way It's a secret")

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by Kritika")
 
        elif 'reason for your creation' in query:
            speak("I was created as a Minor project by my friend Kritika ")

        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop me from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "/")
            speak("You can now take a look at the location")
 
        elif "good morning" in query:
            speak("A warm" + query)
            speak("Every Morining is a fresh start for better tomorrow! So start fresh master!")

        elif 'email to jagatpal' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry my friend! I'm not able to process your request of sending email")

        elif "write a note" in query or "take a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('amara.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            speak("I've written the note!")
         
        elif "show note" in query or "show me note" in query:
            speak("Showing Notes")
            file = open("amara.txt", "r") 
            print(file.read())
            speak(file.read())

        elif "weather" in query:
            # Google Open weather website
            # to get API of Open weather 
            api_key = "your-api-key"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url+"q="+city_name+"&appid="+api_key
            response = requests.get(complete_url) 
            x = response.json() 
             
            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"] 
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"] 
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
                speak(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description)) 
             
            else: 
                speak(" City Not Found ")

        elif "send message " in query:
                # You need to create an account on Twilio to use this service
                account_sid = 'Account Sid key'
                auth_token = 'Auth token'
                client = Client(account_sid, auth_token)
 
                message = client.messages \
                                .create(
                                    body = takeCommand(),
                                    from_='Sender No',
                                    to ='Receiver No'
                                )
 
                print(message.sid)

        elif 'what can you do' in query:
            speak('I am programmed to minor tasks like'
                  'opening youtube, google chrome, gmail stackoverflow , github, predict time,take a photo,write a note for you, send message, send email,search wikipedia,predict weather' 
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions, or even I can make you laugh!')

        elif "thank you" in query or "thankyou" in query:
            speak("It's my pleasure! In what other way I can help you?")

        elif "bye" in query or "stop" in query or "good bye" in query:
            speak("Ok! Have a good day! Bye!")
            exit()
