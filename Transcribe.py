import speech_recognition as sr
import pyttsx3
import os

r = sr.Recognizer()

with sr.AudioFile('speech.wav') as source:
    audio = r.listen(source)  # read the entire audio file
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + text)
