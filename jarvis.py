import wmi  # windows management information for any kind for information regarding system
import os  # provides functions for interacting with the operating system
import requests  # for making HTTP requests to a specified URL
from time import strftime
import pyttsx3  # text-to-speech conversion library
import sys
import datetime
import speech_recognition as sr
import wikipedia  # ********* to improve wikipedia searching
import webbrowser
import random
import pyautogui     # used to take ss
import psutil  # used to track resource utilization in the system
import subprocess  # used to run other programs
import speedtest as speedtest
from ecapture import ecapture as ec
import pyautogui  # to take screenshot
from time import sleep
import screen_brightness_control as sbc
import pyjokes
import pywhatkit  # to send whatsapp msg
import googletrans
from bs4 import BeautifulSoup  # to pull data out of html or XML files
import openai
import time
from playsound import playsound
from pywikihow import search_wikihow
from PyDictionary import PyDictionary
import turtle
import smtplib      #library to send email
import PyPDF2
from PIL import Image

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


list_of_jokes = ["The three most well known languages in India are English, Hindi, and... JavaScript",
                 "Interviewer... Where were you born?Me in India... Interviewer:.. oh, which part?... Me: What ‘which part’ ..? Whole body was born in India",
                 "how many Indians does it take to fix a lightbulb?Two. One to do the task and other to explain how lightbulbs were actually invented in ancient India",
                 "What do you call bread from India? It's Naan of your business",
                 "Britain: Drive on the left side... Europe and America: Drive on the right side...India: lol what's a 'traffic law'?"]
jokes = len(list_of_jokes) - 1
ran_joke = random.randint(0, jokes)
global name


def speak(audio):  # speak audio
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def bytes_to_mb(bytes):
    KB = 1024  # One Kilobyte is 1024 bytes
    MB = KB * 1024  # One MB is 1024 KB
    return int(bytes / MB)


def wishMe():  # wishes me
    speak("Hey Jarvis here,Whats your name?")
    name = takeCommand().lower()

    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 3:
        speak("I am Your Personal assistant, Jarvis! version 1.0!")
        speak(f"As its too late {name}, better if you sleep early ...")

    elif hour >= 4 and hour < 12:
        speak(f"Good Morning {name}!")
        speak("I am Your Personal assistant, Jarvis! version 1.0!")
    elif hour >= 12 and hour < 17:
        speak(f"Good Afternoon {name} !")
        speak("I am Your Personal assistant, Jarvis! version 1.0!")
    elif hour >= 17 and hour < 19:
        speak(f"Good Evening {name}!")
        speak("I am Your Personal assistant, Jarvis! version 1.0!")
    elif hour >= 19 and hour < 24:
        speak(f"Hello {name} ,I am Your Personal assistant, Jarvis! version 1.0!")
        # good night will be greeted after the task is performed and exit command is given
    return name


def takeCommand():  # takes microphone inout and returns output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed
    except Exception as e:
        # Say that again will be printed in case of improper voice
        speak("Say that again please...")
        return "None"  # None string will be returned
    return query


with open('profile.txt', 'r') as f:
    email = f.readline().strip()
    password = f.readline().strip()

def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(email, password)
    server.sendmail(email, to, content)
    server.close()

def readBooks():
    speak("Enter the path of the file including it's name.")
    filePath = input("Enter the path of the file (including it's name): ")
    try:
        os.startfile(filePath)
        book = open(filePath, 'rb')
        pdfreader = PyPDF2.PdfReader(book)
        pages = len(pdfreader.pages)
        speak(f"Number of pages in this books are {pages}")
        speak("From Which Page I Have To Start Reading ?")
        try:
            Page = takeCommand()
            numPage = int(Page)
        except:
            speak("Sorry Sir, Please Write The Page Number.")
            numPage = int(input("Enter The Page Number: "))
        page = pdfreader.pages[numPage-1]
        text = page.extract_text()
        speak(text)
    except:
        speak("This Book is not Present!")

def NasaNews(API_KEY):
    speak("On which day would you like to know ?")
    Date = input("Enter date as (2022-10-21): ")
    
    speak("Extracting Data From Nasa...")
    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(API_KEY)
    Params = {'date':str(Date)}
    r = requests.get(Url, params = Params)

    Data = r.json()
    print("\n")
    copyR = Data['copyright']
    Info = Data['explanation']
    Title = Data['title']
    Image_Url = Data['url']
    Image_r = requests.get(Image_Url)
    FileName = str(Date) + '.jpg'

    with open(FileName, 'wb') as f:
        f.write(Image_r.content)
    img = Image.open(FileName)
    img.show()

    speak(f"{Title} is copyright by {copyR}\n")
    speak(f"Acoording To Nasa : {Info}")

    print(f"CopyRight by {copyR}\n")
    print(f"Title: {Title}\n")
    print(f"FileName: {FileName}\n")

if __name__ == "__main__":
    name = wishMe()
    speak("How May I Help You?")
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('What you wanna search on it?')
            lookfor = takeCommand()
            results = wikipedia.summary(lookfor, sentences=5)
            source = wikipedia.page(lookfor).url
            speak("According to Wikipedia")
            speak(results)
            speak("You may refer to this url for more info")
            print(source)

        elif 'read books' in query:
            readBooks()

        elif 'nasa news' in query:
            speak('Provide the path of text file having API KEY of NASA Organization.')
            filePath = input('Enter the path of API KEY text file: ')
            try:
                with open(filePath, 'r') as file:
                    API_KEY = file.read().strip()
                    if API_KEY and API_KEY != "None":
                        NasaNews(API_KEY)
            except FileNotFoundError:
                print(f"Error: {filePath} not found.")

        elif 'internet speed' in query:
            st = speedtest.Speedtest()
            dl = bytes_to_mb(st.download())
            up = bytes_to_mb(st.upload())
            speak(
                f'{name} we have {dl} MB per second of DOWNLOAD SPEED and {up} MB per second of UPLOAD SPEED')

        elif 'stop' in query or 'shut up' in query or 'sleep' in query:
            speak('Alright Sir! Ping me up when you need me again')
            sys.exit(0)

        elif 'thank you' in query or 'appreciate' in query:
            speak("It's my duty to assist you anytime sir")


        elif 'open youtube' in query:
            speak("Here We Go")
            webbrowser.open("youtube.com")

        elif 'youtube' in query and 'search' in query:
            speak(f"What Should I Search {name}?")
            search_yt = takeCommand()
            search_yt = search_yt.replace(" ", "+")
            speak("Here We Go")
            webbrowser.open(
                f"https://www.youtube.com/results?search_query={search_yt}")

        elif 'open google' in query:
            speak("Here We Go")
            webbrowser.open("google.com")

        elif 'google' in query and 'search' in query:
            speak(f"What Should I Search {name} ?")
            search_go = takeCommand()
            search_go = search_go.replace(" ", "+")
            speak("Here We Go")
            webbrowser.open(f"https://www.google.com/search?q={search_go}")

        elif 'open instagram' in query:
            speak("Here We Go")
            webbrowser.open("instagram.com")
            
        elif 'relax' in query:
            speak("Relaxing........................")
            w = 500
            h = 500
            food_size = 10
            delay = 100
            
            offsets = {
                "up": (0, 20),
                "down": (0, -20),
                "left": (-20, 0),
                "right": (20, 0)
            }
            
            def reset():
                global snake, snake_dir, food_position, pen
                snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
                snake_dir = "up"
                food_position = get_random_food_position()
                food.goto(food_position)
                move_snake()
                
            def move_snake():
                global snake_dir
            
                new_head = snake[-1].copy()
                new_head[0] = snake[-1][0] + offsets[snake_dir][0]
                new_head[1] = snake[-1][1] + offsets[snake_dir][1]
            
                
                if new_head in snake[:-1]:
                    reset()
                else:
                    snake.append(new_head)
            
                
                    if not food_collision():
                        snake.pop(0)
            
            
                    if snake[-1][0] > w / 2:
                        snake[-1][0] -= w
                    elif snake[-1][0] < - w / 2:
                        snake[-1][0] += w
                    elif snake[-1][1] > h / 2:
                        snake[-1][1] -= h
                    elif snake[-1][1] < -h / 2:
                        snake[-1][1] += h
            
            
                    pen.clearstamps()
            
                    
                    for segment in snake:
                        pen.goto(segment[0], segment[1])
                        pen.stamp()
            
                    
                    screen.update()
            
                    turtle.ontimer(move_snake, delay)
            
            def food_collision():
                global food_position
                if get_distance(snake[-1], food_position) < 20:
                    food_position = get_random_food_position()
                    food.goto(food_position)
                    return True
                return False
            
            def get_random_food_position():
                x = random.randint(- w / 2 + food_size, w / 2 - food_size)
                y = random.randint(- h / 2 + food_size, h / 2 - food_size)
                return (x, y)
            
            def get_distance(pos1, pos2):
                x1, y1 = pos1
                x2, y2 = pos2
                distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
                return distance
            def go_up():
                global snake_dir
                if snake_dir != "down":
                    snake_dir = "up"
            
            def go_right():
                global snake_dir
                if snake_dir != "left":
                    snake_dir = "right"
            
            def go_down():
                global snake_dir
                if snake_dir!= "up":
                    snake_dir = "down"
            
            def go_left():
                global snake_dir
                if snake_dir != "right":
                    snake_dir = "left"
            
            
            screen = turtle.Screen()
            screen.setup(w, h)
            screen.title("Snake")
            screen.bgcolor("blue")
            screen.setup(500, 500)
            screen.tracer(0)
            
            
            pen = turtle.Turtle("square")
            pen.penup()
            
            
            food = turtle.Turtle()
            food.shape("square")
            food.color("yellow")
            food.shapesize(food_size / 20)
            food.penup()
            
            
            screen.listen()
            screen.onkey(go_up, "Up")
            screen.onkey(go_right, "Right")
            screen.onkey(go_down, "Down")
            screen.onkey(go_left, "Left")
            
            
            reset()
            turtle.done()

            # code by PK284---------
        elif 'search flight' in query:
            speak("What is the source of the Flight Sir!!")
            source= takeCommand()
            speak("What is the Destination of the Flight Sir!!")
            destination = takeCommand()
            # speak("What is the Travel date sir Please speak in numberic format")
            # traveldate = takeCommand()
            # webbrowser.open(f"https://www.google.com/search?q={search_go}")
            # webbrowser.open(f"https://www.makemytrip.com/flight/search?itinerary={source}-{destination}-25/01/2023-&tripType=O&paxType=A-1_C-0_I-0&intl=false&=&cabinClass=E")
            webbrowser.open(f"https://www.makemytrip.com/flight/search?itinerary={source}-{destination}-26/01/2023&tripType=O&paxType=A-2_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng")



        elif 'open facebook' in query:
            speak("Here We Go")
            webbrowser.open("facebook.com")

        elif 'open twitter' in query:
            speak("Here We Go")
            webbrowser.open("twitter.com")

        elif 'download youtube videos' in query:
            speak("Here We Go")
            webbrowser.open("en.onlinevideoconverter.pro")

        elif 'open whatsapp' in query:
            speak("Here We Go")
            webbrowser.open("web.whatsapp.com")

        elif 'open reddit' in query:
            speak("Here We Go")
            webbrowser.open("reddit.com")

        elif 'open linkedin' in query:
            speak("Here We Go")
            webbrowser.open("linkedin.com")

        elif 'open pinterest' in query:
            speak("Here We Go")
            webbrowser.open("pinterest.com")

        elif 'open quora' in query:
            speak("Here We Go")
            webbrowser.open("quora.com")

        elif 'open discord' in query:
            speak("Here We Go")
            webbrowser.open("discord.com")

        elif ('open prime video' or 'open amazon prime video') in query:
            speak("Here We Go")
            webbrowser.open("primevideo.com")

        elif ('open netflix') in query:
            speak("Here We Go")
            webbrowser.open("netflix.com")

        elif ('open hotstar') in query:
            speak("Here We Go")
            webbrowser.open("hotstar.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)

        elif 'the date' in query:
            today = datetime.date.today()
            speak(today)

        elif query == 'jarvis':
            speak(f"At Your Service {name}, How can I help you")

        elif 'joke' in query:
            URL = 'https://v2.jokeapi.dev/joke/Any'
            response = requests.get(URL)
            data = response.json()
            if response.status_code == 200:
                speak(data['setup'])
                speak(data['delivery'])
            else:
                speak(list_of_jokes[ran_joke])

        elif "volume up" in query:
            pyautogui.press("volumeup")
            speak("volume upped")
            sleep(1)
            speak("anything else for which I may assist you!")

        elif "volume down" in query:
            pyautogui.press("volumedown")
            speak("volume lowered")
            sleep(1)

            speak("anything else for which i may assist you")

        elif 'battery' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f'{name} our System still has {percentage} percent battery')
            if percentage >= 75:
                print("\U0001F601")
                speak(f'{name} we have enough power to continue our work!')
            elif percentage >= 40 and percentage < 75:
                speak(
                    f'{name} we should think of connecting our system to the battery supply!')
            elif percentage <= 40 and percentage >= 15:
                speak(
                    f"{name} we don't have enough power to work through!... Connect now sir!")
            elif percentage < 15:
                speak(
                    f'{name} we have very low power!... Our System may Shutdown anytime soon!...')

        elif "mute" in query:

            if count==0:
                pyautogui.press("volumemute")
                speak("volume muted")
                sleep(1)
                count = 1

            elif count == 1:
                pyautogui.press("volumemute")
                speak("Voluble Now")
                sleep(1)
                count = 0

            speak("anything else for which i may assist you")

        elif "brightness" in query:
            try:
                current = sbc.get_brightness()
                bright = int(takeCommand())
                set = sbc.set_brightness(bright)
                speak(f"brightness set to {set} percent")
                sleep(1)
                speak("anything else for which i may assist you...")
            except Exception as e:
                print(e)
                speak("error")

        elif 'todo' in query or 'to do' in query:
            if 'add' in query or 'create' in query:
                with open('todo.txt', 'a') as f:
                    todo_w = takeCommand()
                    f.write(f"{todo_w}\n")
                speak("To Do is updated successfully !")

            elif 'read' in query or 'tell' in query:
                with open('todo.txt', 'r') as f:
                    todo_r = f.read()
                    if todo_r == "":
                        todo_r = "No Pendning Tasks "
                    speak(todo_r)

            elif 'erase' in query or 'remove all' in query or 'clear' in query:
                with open("todo.txt", "w") as f:
                    f.write("")
                speak("All Tasks has been cleared!")

        elif 'open spotify' in query:
            speak("Opening spotify")
            webbrowser.open("spotify.com")
            
        elif 'screenshot' in query:
            sc = pyautogui.screenshot()
            sc.save('pa_ss.png')
            speak("Screenshot taken successfully.")    

        elif "translate" in query:
            translator = googletrans.Translator()
            lang = ['en', 'ta', 'te', 'kn', 'ml']
            # To Print all the languages that Google Translator Support
            # Command to print Languages Supported
            # print(googletrans.LANGUAGES)
            speak(f"{name} please tell me the Sentence that you want me to translate")
            text = takeCommand().lower()
            speak(
                "Please choose a Source Language by pressing a number from the following List!")
            print(
                " english --->  1  Tamil ---> 2  Telugu ---> 3  Kannada ----> 4  Malayalam ---> 5")
            numberS = int(input("Enter here: "))
            speak(
                "Please choose a Destination Language by pressing a number from the following List!")
            print(
                " english --->  1  Tamil ---> 2  Telugu ---> 3  Kannada ----> 4  Malayalam ---> 5")
            numberD = int(input("Enter here: "))
            translated = translator.translate(
                text, src=lang[numberS - 1], dest=lang[numberD - 1])
            print(translated.text)
            print("Legibility is:",
                  (translated.extra_data['confidence']) * 100, "%")

        elif "log off" in query or "sign out" in query:
            speak(
                "Ok , your pc will log off in 10 seconds! make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis-camera", "img.jpg")

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What is the name of the city?")
            city_name = takeCommand()

            print(f"{city_name} whether conditions : ")

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"] - 273.15
                current_temperature = float('%.2f' % current_temperature)
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in Celcius unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in Celcius unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak("Can't find details about this city")

        elif "current news" in query or "latest news" in query:
            url = "https://www.indiatoday.in/india"
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            # Find all the headlines on the page
            headlines = soup.find_all("h2")
            for headline in headlines[:4]:
                print(headline.text)
                speak(headline.text)

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I am a human creation built by all sets of knowledge of humans.I am nothing without humans")


        elif "initiate" in query or "chat" in query or "Veronica" in query or "gpt" in query:
            def GPT():
                speak("Connecting to Veronica")

                # Enter API KEY or Leave blank if you don't want to use this function
                API_KEY = ""
                openai.api_key = API_KEY
                if API_KEY == "":
                    print("Please Enter the API Key!")
                    speak("Please Enter the API Key!")
                while API_KEY != "":
                    engine1 = pyttsx3.init()
                    voices = engine1.getProperty('voices')
                    engine1.setProperty('voice', voices[1].id)
                    r = sr.Recognizer()
                    mic = sr.Microphone(device_index=1)

                    conversation = ""

                    user_name = str(input("Enter your name: "))
                    bot_name = "Veronica"
                    print("Hey," + user_name)

                    while True:
                        with mic as source:
                            print("\nlistening...")
                            r.adjust_for_ambient_noise(source, duration=0.2)
                            audio = r.listen(source)
                        print("no longer listening.\n")

                        try:
                            user_input = r.recognize_google(audio)
                        except:
                            continue

                        prompt = user_name + ": " + user_input + "\n" + bot_name + ": "

                        conversation += prompt  # allows for context
                        # fetch response from open AI api
                        response = openai.Completion.create(engine='text-davinci-003', prompt=conversation,
                                                            max_tokens=50)
                        response_str = response["choices"][0]["text"].replace("\n", "")
                        response_str = response_str.split(user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

                        conversation += response_str + "\n"
                        print(response_str)
                        engine1.say(response_str)

                        prompt = user_name + ": " + user_input + "\n" + bot_name + ": "

                        conversation += prompt  # allows for context
                        # fetch response from open AI api
                        response = openai.Completion.create(
                            engine='text-davinci-003', prompt=conversation, max_tokens=50)
                        response_str = response["choices"][0]["text"].replace(
                            "\n", "")
                        response_str = response_str.split(
                            user_name + ": ", 1)[0].split(bot_name + ": ", 1)[0]

                        conversation += response_str + "\n"
                        print(response_str)
                        engine1.say(response_str)
                        engine1.runAndWait()


            GPT()

        elif 'news' in query:
            api_key = '9bb9b456bf124f80aba6a0e09cc2f811'
            URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + api_key

            resp = requests.get(URL)
            if resp.status_code == 200:
                data = resp.json()
                news = data['articles'][0]
                speak(news['title'])
                speak(news['description'])
            else:
                speak("Cannot find a news at this moment")


        elif "ip address" in query:
            ip = requests.get('https://api.ipify.org').text
            print(ip)
            speak(f"Your ip address is {ip}")

        elif "switch the window" in query or "switch window" in query:
            speak(f"Okay {name}, Switching the window")
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.keyUp("alt")
        elif 'screenshot' in query:
            speak("Taking screenshot")
            times = time.time()
            name_img = r"{}.png".format(str(times))
            img = pyautogui.screenshot(name_img)
            speak("Done!")
            img.show()

        elif "system" in query:

            c = wmi.WMI()
            my_system = c.Win32_ComputerSystem()[0]
            speak(f"Manufacturer: {my_system.Manufacturer}")
            speak(f"Model: {my_system.Model}")
            speak(f"Name: {my_system.Name}")
            speak(f"NumberOfProcessors: {my_system.NumberOfProcessors}")
            speak(f"SystemType: {my_system.SystemType}")
            speak(f"SystemFamily: {my_system.SystemFamily}")

        elif 'how to' in query:
            try:
                # query = query.replace('how to', '')
                max_results = 1
                data = search_wikihow(query, max_results)
                # assert len(data) == 1
                data[0].print()
                speak(data[0].summary)
            except Exception as e:
                speak('Sorry, I am unable to find the answer for your query.')
                

        elif 'set alarm' in query:
            speak(
                "Tell me the time to set an Alarm. ")
            speak("How do you want to set time in ,like hours/minutes/second")
            a_info = takeCommand()
            if('hours' in a_info):
                speak("Tell me time in hours!")
                a_info=int(input("Type it"))
                # a_info = int(takeCommand())
                speak(f"Alarm set for {a_info} hours")
                time.sleep(a_info *3600)
            elif('minutes' in a_info):
                speak("Tell me time in minutes!")
                a_info = int(input("Type it"))
                # a_info = int(takeCommand())
                time.sleep(a_info * 60)
            else:
                speak("Tell me time in seconds!")
                a_info = int(input("Type it"))
                # a_info = int(takeCommand())
                time.sleep(a_info)

            # playsound('Alarm.mp3')
            speak("Hi I am back!!! Wake Up Wake Up Wake Up Wake Up Wake Up Wake Up!!")

        elif 'meaning' in query:
            speak(f"Which word do you want me to define {name}?")
            queryword = takeCommand().lower()


            meaning = PyDictionary.meaning(queryword)

            for i in meaning:
                print(meaning[i])
                speak("Sir the meaning is  ", str(meaning[i]))

        elif 'generate image' in query or 'image with ai' in query or 'image with artificial intelligence' in query:
            speak("What kind of photo do you want to generate?")
            imageinfo = takeCommand()
            if imageinfo == "":
                pass
            else:
                speak("just wait a bit! I'm processing it!")
                response = openai.Image.create(
                    prompt=imageinfo, n=1, size="1024x1024")
                image_url = response['data'][0]['url']
                webbrowser.open(image_url)
                speak(f"Here is is!! {imageinfo}")
                print(f"Here is is!! {imageinfo}")

        elif 'quit' in query or 'exit' in query or 'close' in query or 'bye' in query:
            speak(f"Thank you for using Jarvis {name}")
            if 19 <= int(datetime.datetime.now().hour) < 24:
                speak(f"Have a very Good Night {name} and sweet dreams!")
            else:
                speak(f"See you soon,have a very Good Day {name}!")
            exit()


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("What is the recipient's email address?")
                to = takeCommand()
                sendemail(to,content)
                speak("email has been sent.")

            except Exception as e:
                print(e)
                speak("Unable to send email.")


        speak("What do you want to continue with?")
