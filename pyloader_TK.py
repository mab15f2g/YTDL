# make executable tutorial
# https://datatofish.com/executable-pyinstaller/

import tkinter as tk
from tkinter import Checkbutton
import subprocess


root= tk.Tk()

command = ["youtube-dl.exe"]


canvas1 = tk.Canvas(root, width = 600, height = 300)
canvas1.pack()

def download ():  
    #first test
    command.append("--help")
    print(command)
    #subprocess.call(command)
    label1 = tk.Label(root, text= 'Finished!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

button1 = tk.Button(text='Click Me',command=download, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)



root.mainloop()