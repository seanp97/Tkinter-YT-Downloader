## Import YouTube dl
##Import path
## Import Tkinter

from __future__ import unicode_literals
from pathlib import Path
import os
from tkinter import *
import sys
import tkinter
from youtube_dl import YoutubeDL

path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

def YTDownload():
    ytURL = Entry.get(ytEnt)
    ydl_opts = {
    'format': 'best',
    'outtmpl': path_to_download_folder + '/' + '%(title)s '+'.mp3',
    'noplaylist': True,
    'extract-audio': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(ytURL, download=True)

app = Tk()
app.title("Youtube Downloader")
app.geometry("900x450")

ytLabel = Label(app, text="Enter Youtube URL to download", pady=10, padx=10)
ytLabel.grid(column=0, row=0)

ytEnt = Entry(app, bd=5)
ytEnt.grid(column=0, row=1)

ytBtn = Button(app, command=YTDownload, text="Download")
ytBtn.grid(column=0, row=2)

app.mainloop()