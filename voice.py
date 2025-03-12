import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr  #pip install speechRecognition
import wikipedia   #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Cyrus sir. Please tell me how can i help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User_said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again Please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('210303125055@paruluniversity.ac.in','password')
    server.sendmail('suryamahajan064@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    # speak("Surya is an intelligent boy")
    wishMe()
    while True:
        query = takeCommand().lower()
        # Logic to execute tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("Youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open amazon' in query:
            webbrowser.open("amazon.in")
            
        elif 'open news' in query:
            webbrowser.open("news.google.co.in")
            
        elif 'open StackOverflow' in query:
            webbrowser.open("stackoverflow.com")
            
            
        elif 'play music' in query:
            music_dir = ''
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is {strTime}")
        
        
        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to surya' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "suryamahajan064@gmail.com"
                sendEmail(to, content)
                speak("Email has been Sent")
            except Exception as e:
                speak("Sorry My friend Surya Bro, I am not able to send the email")
        elif 'exit' in query:
            break
        
            