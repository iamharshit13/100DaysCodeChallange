
#This will narrate the whole text in the rpogram execution itself
'''import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


f = open('book.txt')
x = f.read().lower()

speak(x)
'''


#This will read the text and then save it to an audio file in the format mentioned like mp3/wav etc
from gtts import gTTS
import os
f = open('book.txt')
x= f.read().lower()
language = 'en'
audio = gTTS(text=x,lang=language,slow=False)

audio.save('book.mp3')
