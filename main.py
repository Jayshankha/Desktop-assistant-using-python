import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


#Taking voice from my system
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice", voices.id)
engine.setProperty("rate", 150)

# Speak function

def speak(text):

   """ This function takes text and returns voice

   Args:
       text (_type_): string
   
   """
    engine.say(text)
    engine.runAndWait()

