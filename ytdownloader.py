from tkinter import *
import tkinter as tk
import subprocess

root = tk.Tk()
root.geometry("600x400")


is_checked_playlist = tk.IntVar()
is_checked_error = tk.IntVar()


# Dowload button click methode
def download():
    print("________")
    print(scale.get())
    
    comm = " "
    comm = comm.join(create_command())
    print(comm)
    # execute dl.exe
    subprocess.call(comm)




# concate the options
def set_options():

    options = []
    if is_checked_playlist.get() == 1:
        options.append("--playlist")
    if is_checked_error.get() == 1:
        options.append("-i")
    #options.append("--audio-quality")
    #options.append(str(scale.get()))
    return options

# get link from textfield
def get_link():
    
    link = e1.get()

    return link

# conates the command
def create_command():
    command = ["dl.exe -x --audio-format mp3"]
    link = get_link()
    options = set_options()
    command.append(link)
    command = command + options

    return command


# Labels
label1 = Label(root, text="YT Link").grid(row=0)
label2 = Label(root, text="Quality").grid(row=5,column=1, sticky=W)

# Entry fileds 
e1 = tk.Entry(root, width=50)
e1.insert(0,"https://www.youtube.com/watch?v=2uRO_FabHRo")
e1.grid(row=0, column=1)
# Checkbuttons
check_playlist = Checkbutton(root, text = "Playlist?" , variable=is_checked_playlist)
check_playlist.grid(row=1, column=1, sticky=W)
check_error = Checkbutton(root, text = "Ignore Errors?", variable=is_checked_error )
check_error.grid(row=2, column=1, sticky=W)
checkbutton3 = Checkbutton(root, text = "Bypass geoblock?" )
checkbutton3.grid(row=3, column=1, sticky=W)

# Download button
button1 = Button(root, text = "Download",command=download, bg='blue', fg='white')
button1.grid(sticky=E + S)
# Quality slider
scale = Scale(root, from_=128, to=320, orient=HORIZONTAL)
scale.grid(row=5,column=1)
root.mainloop()