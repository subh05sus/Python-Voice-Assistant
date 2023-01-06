import pyttsx3
import response

from voice_utils import speak, speech_reconnize

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

list_of_jokes = [
    "The three most well known languages in India are English, Hindi, and... JavaScript",
    "Interviewer... Where were you born?Me in India... Interviewer:.. oh, which part?... Me: What ‘which part’ ..? Whole body was born in India",
    "how many Indians does it take to fix a lightbulb?Two. One to do the task and other to explain how lightbulbs were actually invented in ancient India",
    "What do you call bread from India? It's Naan of your business",
    "Britain: Drive on the left side... Europe and America: Drive on the right side...India: lol what's a 'traffic law'?",
]

if __name__ == "__main__":

    response.wish_me()
    speak(engine, "How may I help you sir?")

    while True:

        query = speech_reconnize().lower()

        if "wikipedia" in query:
            response.wikipedia_search()

        elif "open youtube" in query:
            response.open_youtube()

        elif {"youtube", "search"} in query:
            response.youtube_search()

        elif "open google" in query:
            response.open_google()

        elif {"google", "search"} in query:
            response.google_search()

        elif "open instagram" in query:
            response.open_instragram()

        elif "open facebook" in query:
            response.open_facebook()

        elif "open twitter" in query:
            response.open_twitter()

        elif "download youtube videos" in query:
            response.open_youtube_video_converter()
            
        elif "open spotify" in query:
            response.open_spotify()

        elif "the time" in query:
            response.get_time()

        elif "the date" in query:
            response.get_date()

        elif query == "jarvis":
            response.jarvis_speech()

        elif "joke" in query:
            response.tell_joke(list_of_jokes)

        elif "volume up" in query:
            response.volume_up()
            
        elif "volume down" in query:
            response.volume_down()
            
        elif "mute" in query:
            response.mute()
            
        elif "brightness" in query:
            response.set_brightness()

        elif "todo" in query or "to do" in query:
            response.todo()

        elif "jarvis quit" in query or "exit" in query or "close" in query:
            speak(engine, "Thanks you for using Jarvis Sir")
            exit()
