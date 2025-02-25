import tkinter as tk
import subprocess
from tkinter import * 
from tkinter import ttk


root = tk.Tk()
root.title('Ernstl Downloader')
root.geometry("600x400")

audio_choices = ["aac","flac", "mp3", "m4a", "opus", "vorbis","wav"]
format_choise = []

is_checked_playlist = tk.IntVar()
is_checked_error = tk.IntVar()
is_checked_bypass = tk.IntVar()

# Dowload button click methode
def download():   
    comm = " "
    comm = comm.join(create_command())
    print(comm)
    # execute dl.exe
    subprocess.call(comm)

# Concate the options
def set_options():

    options = []
    options.append("--audio-format")
    options.append(combobox1.get())

    if is_checked_playlist.get() == 1:
        options.append("--playlist")
    if is_checked_error.get() == 1:
        options.append("-i")
    if is_checked_bypass.get() == 1:
        options.append("--geo-bypass")
    
    options.append("-r")
    options.append(str(scale2.get()*1000))    
    options.append("--audio-quality")
    options.append(str(scale.get()))
    return options

# Get link from textfield
def get_link():    
    link = e1.get()

    return link

# Conates the command
def create_command():
    command = ["dl.exe -x  -o /downloaded/%(title)s.%(ext)s"]
    link = get_link()
    options = set_options()
    command.append(link)
    command = command + options

    return command


# Labels
label1 = Label(root, text="YT Link").grid(row=0)
label2 = Label(root, text="Quality  Format in Kbit/s").grid(row=5,column=1, sticky=W)
label3 = Label(root, text="Audio Format").grid(row=4,column=1, sticky=W)
label4 = Label(root, text="Limit Download in kbyte/s").grid(row=6,column=1, sticky=W)

# Entry fileds 
e1 = tk.Entry(root, width=80)
e1.insert(0,"https://www.youtube.com/watch?v=2uRO_FabHRo")
e1.grid(row=0, column=1)

# Checkbuttons
check_playlist = ttk.Checkbutton(root, text = "Playlist?" , variable=is_checked_playlist)
check_playlist.grid(row=1, column=1, sticky=W)
check_error = ttk.Checkbutton(root, text = "Ignore Errors?", variable=is_checked_error)
check_error.grid(row=2, column=1, sticky=W)
checkbutton3 = ttk.Checkbutton(root, text = "Bypass geoblock?",variable=is_checked_bypass )
checkbutton3.grid(row=3, column=1, sticky=W)

# Combobox
combobox1 = ttk.Combobox(root, values = audio_choices)
combobox1.current(2)
combobox1.grid(row=4, column=1)

# Slider
scale = Scale(root, from_=128, to=320, orient=HORIZONTAL)
scale.grid(row=5,column=1)
scale2 = Scale(root, from_=256, to=10000, orient=HORIZONTAL)
scale2.grid(row=6,column=1)

# Download button
button1 = ttk.Button(root, text = "Download",command=download)
button1.grid(row=7, column=1,sticky=W)

# Main loop
root.mainloop()