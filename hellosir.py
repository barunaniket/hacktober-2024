import datetime
import random
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Index 1 usually represents a female voice

greetings = [
    "Hello sir!",
    "Greetings sir!",
    "Wanna fuck sir?",
    "Good day to you sir!",
    "How do you do sir?",
    "So how are you sir?",
    "A pleasure to make your acquaintance sir!"
]

current_time = datetime.datetime.now()
hour = current_time.hour

if 5 <= hour < 12:
    greeting = "Good morning"
elif 12 <= hour < 17:
    greeting = "Good afternoon"
elif 17 <= hour < 24:
    greeting = "Good evening"
    
random_greeting = random.choice(greetings)

text_to_speak = f"{random_greeting}. The current time is {current_time.strftime('%H:%M:%S')}."
engine.say(text_to_speak)
engine.runAndWait()