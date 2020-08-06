# make executable tutorial
# https://datatofish.com/executable-pyinstaller/
# https://datatofish.com/entry-box-tkinter/ Textbox
import tkinter as tk
from tkinter import Checkbutton , Frame
import subprocess


root= tk.Tk()

# downloader command
command = ["youtube-dl.exe"]


canvas1 = tk.Canvas(root, width = 600, height = 300)
canvas1.grid(row=0,column=1)

frame = Frame(root)
frame.grid(row=0,column=0, sticky="n")


##
# Dowload button click methode
##
def download ():  
    #get link from textfield  
    link =  entry1.get()    
    print(command)
    print(command)
    #subprocess.call(command)
    label1 = tk.Label(root, text= link, fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    

##
# Labels
##

label1 = tk.Label(root, text='Youtube Dowloader')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 15, window=label1)

label2 = tk.Label(text='Paste link here')
label2.config(font=('helvetica', 10))
canvas1.create_window(50, 40, window=label2)

##
# Buttons
##
button1 = tk.Button(text='Click Me',command=download, bg='brown',fg='white')
button1.grid(row=1, column=1)
canvas1.create_window(150, 150, window=button1)

##
# Textfield
##
entry1 = tk.Entry(root) 
entry1.grid(row=1, column=1)
canvas1.create_window(250, 40, window=entry1)



root.mainloop()