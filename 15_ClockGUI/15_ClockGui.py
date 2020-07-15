from datetime import datetime
import pytz

from tkinter import *


root = Tk()
root.geometry("500x250")
#root.configure(bg='teal')
#root['bg'] = 'teal'
root['background']='black'

def times():
    home = pytz.timezone('Asia/Kolkata')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock.config(text = current_time)
    name.config(text= "India")

    home = pytz.timezone('Australia/Victoria')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock1.config(text=current_time)
    name1.config(text="Australia")

    home = pytz.timezone('America/New_York')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock2.config(text=current_time)
    name2.config(text="USA")

    home = pytz.timezone('Africa/Timbuktu')
    local_time = datetime.now(home)
    current_time = local_time.strftime("%H:%M:%S")
    clock3.config(text=current_time)
    name3.config(text="Africa")
    clock.after(200,times)


name = Label(root,font=("Comic Sans MS",22,"bold"), background="black", foreground="green")
name.place(x=30,y=5)

clock = Label(root,font=("Comic Sans MS",25,"bold"), background="black", foreground="green")
clock.place(x=10,y=40)

nota = Label(root,text="Hours      Minutes     Seconds",font=("times",10,"bold"), background="black", foreground="green")
nota.place(x=10,y=80)



name1 = Label(root,font=("Comic Sans MS",20,"bold"), background="black", foreground="green")
name1.place(x=330,y=5)

clock1 = Label(root,font=("Comic Sans MS",25,"bold"), background="black", foreground="green")
clock1.place(x=310,y=40)

nota1 = Label(root,text="Hours      Minutes     Seconds",font=("times",10,"bold"), background="black", foreground="green")
nota1.place(x=310,y=80)


name2 = Label(root, font=("Comic Sans MS",20,"bold"), background="black", foreground="green")
name2.place(x=30,y=105)

clock2 = Label(root,font=("Comic Sans MS",25,"bold"), background="black", foreground="green")
clock2.place(x=10,y=140)

nota2 = Label(root,text="Hours      Minutes     Seconds",font=("times",10,"bold"), background="black", foreground="green")
nota2.place(x=10,y=180)


name3 = Label(root,font=("Comic Sans MS",20,"bold"), background="black", foreground="green")
name3.place(x=330,y=105)

clock3 = Label(root, font=("Comic Sans MS",25,"bold"), background="black", foreground="green")
clock3.place(x=310,y=140)

nota3 = Label(root,text="Hours      Minutes     Seconds",font=("times",10,"bold"), background="black", foreground="green")
nota3.place(x=310,y=180)


times()


root.mainloop()



