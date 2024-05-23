import pyttsx3
import speech_recognition as sr
import datetime


#Taking voice from my system
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voice")
#print(voices)
engine.setProperty("voice", voices)
engine.setProperty("rate", 150)

# Speak function

def speak(text):

   """ This function takes text and returns voice
       Args:
       text (_type_): string
   
   """
   engine.say(text) 
   engine.runAndWait()

def takeComand():
    """ this function will recognize voice & return text
    """

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language= "en-in")
            print(f"User said: {query}\n")

        except Exception as e:
            print("say that again please...")
            return "None"
        return query
    

def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Jayshankha. How are you doing")
    
    elif hour>=12 and hour<18:
        speak("Good afternoon Jayshankha. How are you doing")

    else:
        speak("Good evening Jayshankha. How are you doing")
    
    speak("I am JARVIS. Tell me sir how can i help you")