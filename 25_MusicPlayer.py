# mp3 player

from tkinter import *
import pygame
import os

window = Tk()
window.geometry('300x150')
window['background']='black'

pygame.mixer.init()
n = 0

def start_stop():
    global n
    n=n+1

    if n ==1:
        song_name = song_listbox.get()
        pygame.mixer.music.load(song_name)
        pygame.mixer.music.play(0)

    elif(n%2)==0:
        pygame.mixer.music.pause()

    elif(n%2)!=0:
        pygame.mixer.music.unpause()



l1= Label(window,text = "Music Player", font=("Comic Sans MS",22,"bold"), background="black", foreground="green")
l1.grid(row =1,column=1)

b1= Button(window, text='Play/Pause',font=("Comic Sans MS",10,"bold"), background="black", foreground="green", width=20,command=start_stop)
b1.grid(row=4,column=1)


song_list = os.listdir()
song_listbox = StringVar(window)
song_listbox.set("Select Song")

menu = OptionMenu(window,song_listbox,*song_list,)
menu.config(bg = "BLACK")
menu.config(font=("Comic Sans MS",10), background="black", foreground="green")
menu["highlightthickness"]=0
menu.grid(row=4,column=4)

window.mainloop()


