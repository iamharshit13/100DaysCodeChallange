'''import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


f = open('book.txt')
x = f.read().lower()

speak(x)
'''

from gtts import gTTS
import os
f = open('book.txt')
x= f.read().lower()
language = 'en'
audio = gTTS(text=x,lang=language,slow=False)

audio.save('book.mp3')
