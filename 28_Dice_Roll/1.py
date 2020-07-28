import tkinter
import random

# toplevel widget of Tk which represents mostly the main window of an application
root = tkinter.Tk()
root.geometry('500x300')
root.title('Roll Dice')

# label to display dice
label = tkinter.Label(root, text='', font=('Helvetica', 200))

# function activated by button
def roll_dice():
    # unicode character strings for dice
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    # print(f'{random.choice(dice)} {random.choice(dice)}')
    label.configure(text=f'{random.choice(dice)} {random.choice(dice)}')
    label.pack()

# button
button = tkinter.Button(root, text='roll dice',font=('Comic Sans MS', 10 , 'bold italic') ,foreground='white', background='black', command=roll_dice)

# pack a widget in the parent widget
button.pack()

# call the mainloop of Tk
# keeps window open
root.mainloop()