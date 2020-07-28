import tkinter
from PIL import Image, ImageTk
import random
import time

root = tkinter.Tk()
root.geometry('600x500')
root.title('Roll Dice')
root['bg']='black'

dice = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg']

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(root, image=image1)
label2 = tkinter.Label(root, image=image2)
#Reference, if needed
#label1.image = image1
#label2.image = image2
label1.pack(side=tkinter.LEFT)
label2.pack(side=tkinter.RIGHT)


def roll_dice():

    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1)
    # keep a reference
    label1.image = image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label2.configure(image=image2)
    # keep a reference
    label2.image = image2

button = tkinter.Button(root, text='Let\'s Roll' ,font=('Comic Sans MS', 20 , 'bold italic'), foreground='green', background='black', command=roll_dice)

button.pack()

root.mainloop()