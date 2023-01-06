import pyttsx3
import speech_recognition as sr

def speak(engine: pyttsx3.engine.Engine, base_text: str) -> None:
    engine.say(base_text)
    engine.runAndWait()
    
    
def speech_reconnize() -> str:
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")
        
    except sr.UnknownValueError:   
        print("Say that again please...") 
        return "None"
    
    return query