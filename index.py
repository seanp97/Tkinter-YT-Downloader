## Import YouTube dl
##Import path
## Import Tkinter

from __future__ import unicode_literals
from pathlib import Path
import os
from tkinter import *
import sys
import tkinter
from tkinter import messagebox
from youtube_dl import YoutubeDL

backSlash = "\ ".strip()
filePath = ""
isClicked = False

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

def optFilePath():
    global filePath
    filePath = Entry.get(ytOptionalFileEnt)
    messagebox.showinfo('File path chosen', filePath)
    global isClicked
    isClicked = True

def YTDownload():
    ytURL = Entry.get(ytEnt)
    global filePath
    global isClicked

    if filePath == "" or isClicked == False:
        ydl_opts = {
            'format': 'best',
            'outtmpl': path_to_download_folder + '/' + '%(title)s '+'.mp3',
            'noplaylist': True,
            'extract-audio': True,
        }
    else:
        ydl_opts = {
            'format': 'best',
            'outtmpl': filePath + '/' + '%(title)s '+'.mp3',
            'noplaylist': True,
            'extract-audio': True,
        }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            infoDict = ydl.extract_info(ytURL, download=True)
            videoTitle = infoDict.get('title', None)
            if filePath == "" or isClicked == False:
                messagebox.showinfo("Success", "Downloaded at: " + path_to_download_folder + backSlash + videoTitle + ".mp3")
            else:
                messagebox.showinfo("Success", "Downloaded at: " + filePath + backSlash + videoTitle + ".mp3")

    except:
            messagebox.showwarning('Error', 'MP3 File could not be downloaded')



app = Tk()
app.title("Youtube Downloader")
app.geometry("900x450")

ytOptionalFilePathLabel = Label(app, text="Enter optional folder path to add MP3's to", pady=10, padx=10,  font='Helvetica 8 bold')
ytOptionalFilePathLabel.grid(column=0, row=0)
ytOptionalFileEnt = Entry(app, bd=5)
ytOptionalFileEnt.grid(column=0, row=1)
ytOptionalBtn = Button(app, bd=1, text="Submit", command=optFilePath)
ytOptionalBtn.grid(column=0, row=2)

ytLabel = Label(app, text="Enter Youtube URL to download", pady=10, padx=10,  font='Helvetica 16 bold')
ytLabel.grid(column=0, row=3)

ytEnt = Entry(app, bd=5)
ytEnt.grid(column=0, row=4)

ytBtn = Button(app, command=YTDownload, bd=1, text="Download")
ytBtn.grid(column=0, row=5)

app.mainloop()
