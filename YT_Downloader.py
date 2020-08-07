# make executable tutorial
# https://datatofish.com/executable-pyinstaller/
# https://datatofish.com/entry-box-tkinter/ Textbox
import tkinter as tk
from tkinter import Checkbutton , Frame, IntVar, Scale, HORIZONTAL, Text
import subprocess
import sys



main= tk.Tk()

root = Frame(main)
root.grid(row=0,column=0, sticky="n")

col1 = 150
col2 = 250

row1 = 50
row2 = 100
row3 = 150
row4 = 200
row5 = 250
row6 = 300
testlink = "https://www.youtube.com/watch?v=2uRO_FabHRo"
testplaylist= "https://www.youtube.com/playlist?list=PLkdKYxSQmXhOkpa105w1vwPOmv3fBshYv"

canvas1 = tk.Canvas(root, width = 800, height = 400)
canvas1.grid(row=0,column=1)

frame = Frame(root)
frame.grid(row=0,column=0, sticky="n")

is_checked_playlist = tk.IntVar()



##
# Dowload button click methode
##
def download ():  
    comm = " "
    comm = comm.join(create_command())
    print(comm)
    # execute youtube-dl.exe
    subprocess.call(comm)
     

# concate the options
def set_options():
    
    options = []
    if is_checked_playlist.get() == 1:
        options.append("--playlist")
    

    options.append("--audio-quality")
    options.append(str(scaler.get()))
    return options

#get link from textfield  
def get_link():
    link = entry1.get()

    return link

#conates the command
def create_command():
    command = ["dl.exe -x --audio-format mp3"]
    link = get_link()
    options = set_options()
    command.append(link)
    command = command + options
        
    return command




##
# Labels
##

#label1 = tk.Label(root, text='Youtube Dowloader')
#label1.config(font=('helvetica', 14))
#canvas1.create_window(200, 15, window=label1)

#label2 = tk.Label(text='Paste link here')
#label2.config(font=('helvetica', 8))
#canvas1.create_window(col1, row2, window=label2)

label3 = tk.Label(text='Playlist?')
label3.config(font=('helvetica', 8))
canvas1.create_window(col1, row3, window=label3)

label4 = tk.Label(text='Quality?')
label4.config(font=('helvetica', 8))
canvas1.create_window(col1, row4, window=label4)

##
# Buttons
##
button1 = tk.Button(text='Download',command=download, bg='brown',fg='white')
canvas1.create_window(col1, row6, window=button1)

##
# Checkbox
##
check_playlist = Checkbutton(root,variable=is_checked_playlist)
canvas1.create_window(col2, row3, window=check_playlist)

##
# Textfield
##
entry1 = tk.Entry(root) 
entry1.insert(0,"Paste link here")
canvas1.create_window(col1, row1, window=entry1)

##
# Scaler
##
scaler = Scale(root, from_=128, to=320, orient=HORIZONTAL)
canvas1.create_window(col2, row4, window=scaler)

root.mainloop()