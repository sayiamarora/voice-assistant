
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.say("hello sir ")
engine.say("how are you ")
engine.runAndWait()
try:
    with sr.Microphone() as source:
        print("speak now____")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except:
    pass   



