import time
import random
import pyautogui
import wikipedia

import datetime as dt
import webbrowser as wb
import screen_brightness_control as sbc

from jarvis import engine, query
from voice_utils import speak, speech_reconnize

def wish_me() -> None:
    
    hour = dt.datetime.now().hour
    
    if hour in range(0, 4):
        speak("It's Late Night Sir!, You should sleep right now")
        return

    elif hour in range(4, 12):
        speak("Good Moring Master!")
        return
        
    elif hour in range(12, 17):
        speak("Good Afternoon Sir !")
        return
        
    elif hour in range(17, 19):
        speak("Good Evening !")
        return
        
    elif hour in range(19, 24):
        speak("Good Night Sir!")
        return

    speak(engine, "I'm Your Personal assistant, Jarvis! version 1.0")
    

def jarvis_speech() -> None:
    speak(engine, "At Your Service Sir, How can I help you")
    

def tell_joke(list_of_jokes: list[str]) -> None:
    speak(engine, random.choice(list_of_jokes))
    
    
##### Open website #####
    
def open_google() -> None:
    speak(engine, "Here We Go")
    wb.open("google.com")


def open_instragram() -> None:
    speak(engine, "Here We Go")
    wb.open("instagram.com")
    
    
def open_facebook() -> None:
    speak(engine, "Here We Go")
    wb.open("facebook.com")
    
    
def open_spotify() -> None:
    speak(engine, "Opening spotify")
    wb.open("spotify.com")
    
    
def open_twitter() -> None:
    speak(engine, "Here We Go")
    wb.open("twitter.com")
    
    
def open_youtube() -> None:
    speak(engine, "Here We Go")
    wb.open("youtube.com")

def open_youtube_video_converter() -> None:
    speak(engine, "Here We Go")
    wb.open("en.onlinevideoconverter.pro")


##### Search #####

def google_search() -> None:
    
    speak(engine, "What Should I Search Sir ?")
    
    search_data = speech_reconnize().replace(" ", "+")
    
    speak(engine, "Here We Go")
    wb.open(f"https://www.google.com/search?q={search_data}")
    
    
def wikipedia_search() -> None:
    
    speak(engine, 'Searching in Wikipedia')
    
    query.replace("according to wikipedia", "")
    
    results = wikipedia.summary(query, sentences=2)
    speak(engine, "Accoring to Wikipedia")
    
    print(results)
    speak(engine, results)
    
    
def youtube_search() -> None:
    
    speak(engine, "What Should I Search Sir?")
    search_yt = speech_reconnize().replace(" ", "+")
    
    speak(engine, "Here We Go")
    wb.open(f"https://www.youtube.com/results?search_query={search_yt}")
    

##### Date time #####    
    
def get_time() -> None:
    strTime = dt.datetime.now().strftime("%H:%M:%S")
    speak(engine, strTime)
    
    
def get_date() -> None:
    today = dt.date.today()
    speak(engine, today)
    
    
##### Volume Control #####
    
def volume_up() -> None:
    
    pyautogui.press("volumeup")
    speak(engine, "volume upped")
    
    time.sleep(1)
    speak(engine, "anything else for which i may assist you")
    

def volume_down() -> None:
    
    pyautogui.press("volumedown")
    speak(engine, "volume lowered")
    
    time.sleep(1)
    speak(engine, "anything else for which i may assist you")
    
    
def mute() -> None:
    
    pyautogui.press("volumemute")
    speak(engine, "volume muted")
    
    time.sleep(1)
    speak(engine, "anything else for which i may assist you")
    
    
##### Brightness #####

def set_brightness() -> None:
    
    try:
        
        bright = int(speech_reconnize())
        set = sbc.set_brightness(bright)
        
        speak(engine, f"brightness set to {set} percent")
        
        time.sleep(1)
        speak(engine, "anything else for which i may assist you")
        
    except Exception as e:
        print(e)
        speak(engine, "Error")
        
        
##### Todo #####
def todo() -> None:
    
    if "add" in query or "create" in query:
        
        with open("todo.txt", "a+") as f:
            todo_w = speech_reconnize()
            f.write(f"{todo_w}\n")
            
        speak(engine, "To Do is updated successfully !")
        
    elif "read" in query or "tell" in query:
        
        with open("todo.txt") as f:
            todo_r = f.read()
            
            if not todo_r.strip:
                todo_r = "No Pendning Tasks Sir"
                
            speak(engine, todo_r)

    elif "erase" in query or "remove all" in query or "clear" in query:
        
        with open("todo.txt", "w") as f:
            f.write("")
            
        speak(engine, "All Tasks has been cleared, Sir!")