# import os
import random
import pyjokes
import pyttsx3



engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
# music_dir = 'C:\\Users\\sahas\\OneDrive\\Desktop\\Subhadip\\Media\\Fav one'
# songs = os.listdir(music_dir)
# a=len(songs)-1
# num1= random.randint(0,a)
# print(num1)


# email_dict={
#     "me":"sahasubhadip54@gmail.com",
#     "baba":"sasti.saha75@gmail.com",
#     "didi":"sahasnehafkk@gmail.com"}

# print(email_dict.get("me"))

# list_of_jokes = ["ek aadamee ne facebook par post kiya, ki aaj main chhat par sooonga. bas phir kya tha mohalle ke 25-30 machchharon ne laik kar diya. aur usake baad do choron ne bhee kaam bata diya. ab vah chhat par nahin sota hai","The three most well known languages in India are English, Hindi, and... JavaScript","Interviewer Where were you born?Me in IndiaInterviewer: oh, which part?Me: What ‘which part’ ..? Whole body was born in India","how many Indians does it take to fix a lightbulb?Two. One to do the task and other to explain how lightbulbs were actually invented in ancient India","What do you call bread from India? It's Naan of your business","Britain: Drive on the left side... Europe and America: Drive on the right side...India: Lmao what's a 'traffic law'?"]
# jokes = len(list_of_jokes)-1
# ran_joke=random.randint(0,jokes)
# print(list_of_jokes[ran_joke])

def speak(audio): #speak audio
    engine.say(audio)
    engine.runAndWait()


speak("nikal lau rae, paeheli fursat mae nikal")