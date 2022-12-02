import os
from time import strftime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

email_dict={
    "me":"sahasubhadip54@gmail.com",
    "baba":"sasti.saha75@gmail.com",
    "didi":"sahasnehafkk@gmail.com"}

def speak(audio): #speak audio
    engine.say(audio)
    engine.runAndWait()

def wishMe(): #wishes me
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=3:
        speak("Soja Lau rae, teri baandi nahi hae, hahahaha")


    elif hour>=4 and hour<12:
        speak("Uth gaya Lodu chand")
    elif hour>=12 and hour<17:
        speak("Saalae abhi sonae ka time hae mera, matt jagaya kar mekko bc!")
    elif hour>=17 and hour<19:
        speak("paar nae baith lodu")
    elif hour>=19 and hour<24:
        speak("lau rae soja bc")

    if hour>=0 and hour<=4:
        pass
    else:
        speak("Hemlo domst, Mein hu Jarvis! Jarvis to chu tia hae ! mein hu badass jarvis! bol lau rae kya kar sakta hu tere liye, english mein bolna, developer chu tia hae, hindi voice nahi dala")

def takeCommand(): #takes microphone inout and returns output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition
        print(f"User said: {query}\n")  #User query will be printed
    except Exception as e:   
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendEmail(to, econtent): #sending email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('subhadipsudi@gmail.com', 'Sudi@1234')
    server.sendmail('subhadipsudi@gmail.com', to, econtent)
    server.close()

if __name__ == "__main__":
    wishMe()
    speak("Jaldi bol! kaal subha panvel nikalna hae")
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Dhunndh raaha hu')
            query = query.replace("according to wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("Accoring to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Here We Go")
            webbrowser.open("youtube.com")
        elif 'youtube' in query and 'search' in query:
            speak("paehelae baataa raaha hu! porn videos nahi mil lengue")
            search_yt=takeCommand()
            search_yt=search_yt.replace(" ","+")
            speak("Here We Go")
            webbrowser.open(f"https://www.youtube.com/results?search_query={search_yt}")
        elif 'open google' in query:
            speak("Here We Go")
            webbrowser.open("google.com")
        elif 'google' in query and 'search' in query:
            speak("tere baaap ka naukar samajh ke rakha hae mujhe")
            search_go=takeCommand()
            search_go=search_go.replace(" ","+")
            speak("Here We Go")
            webbrowser.open(f"https://www.google.com/search?q={search_go}")
        elif 'open instagram' in query:
            speak("Here We Go")
            webbrowser.open("instagram.com")
        elif 'open facebook' in query:
            speak("Here We Go")
            webbrowser.open("facebook.com")
        elif 'open twitter' in query:
            speak("Here We Go")
            webbrowser.open("twitter.com")
        elif 'download youtube videos' in query:
            speak("Here We Go")
            webbrowser.open("en.onlinevideoconverter.pro")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\sahas\\OneDrive\\Desktop\\Subhadip\\Media\\Fav one'
            songs = os.listdir(music_dir)
            a=len(songs)-1
            ran_num= random.randint(0,a)
            os.startfile(os.path.join(music_dir, songs[ran_num]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'the date' in query:
            today=datetime.date.today()
            speak(today)
        elif 'open downloads' in query:
                downloadPath='C:\\Users\\sahas\\Downloads'
                os.startfile(downloadPath)
        elif 'my important documents' in query:
                downloadPath='F:\\Media'
                os.startfile(downloadPath)
        elif 'my media' in query:
                downloadPath='F:\\Docs'
                os.startfile(downloadPath)
        elif 'code' in query:
                ApplicationPath="C:\\Users\\sahas\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(ApplicationPath)
        elif 'filmora' in query:
                ApplicationPath="C:\\Program Files\\Wondershare\\Filmora9\\Wondershare Filmora9.exe"
                os.startfile(ApplicationPath)
        elif 'chrome' in query:
                ApplicationPath="C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
                os.startfile(ApplicationPath)
        elif 'email' in query:
            try:
                if 'me' in query:
                    to = email_dict.get("me")
                elif 'baba' in query:
                    to = email_dict.get("baba")
                elif 'didi' in query:
                    to = email_dict.get("didi")
                else:
                    to = input("Enter New Email: ")
                
                speak("kya likhu lau rae")
                econtent=takeCommand()
                sendEmail(to, econtent)
                speak("Email has been sent!")
            except Exception as e:
                print("Sorry Sir, I can't send the email")
                speak("lagtaa hae server ki gaand faati paari hae")
        elif query == 'jarvis':
            speak("Gaand mae daal liyo Jarvis")
        elif 'joke' in query:
            speak("teri zin-dagui-saae baari or kya joke hae! hahahahha! destroyed waala meme daal dena please")
        elif 'todo'in query or 'to do' in query:
            if 'add' in query or 'create' in query:
                with open('todo.txt','a') as f:
                    todo_w=takeCommand()
                    f.write(f"{todo_w}\n")
                speak("kaam ho gya")                    
            elif 'read' in query or 'tell' in query:
                with open('todo.txt','r') as f:
                    todo_r=f.read()
                    if todo_r =="":
                        todo_r="No Pendning Tasks Sir"
                    speak(todo_r)
            elif 'erase' in query or 'remove all' in query or 'clear' in query:
                with open("todo.txt","w") as f:
                    f.write("")
                speak("kaam ho gya lau rae !")
        elif 'jarvis quit' in query or 'exit' in query or 'close' in query:
            speak("nikal lau rae, paeheli fursat mae nikal")
            exit()
