from itertools import count
from pytube import YouTube
from pytube import Channel
from pytube import Playlist
import os
from os import path
import shutil
from re import T
import tkinter
from tkinter import *
from tkinter import ttk
import sys
import threading
import time

cd=os.getcwd()
dp='D:\Download\YoutubeDownloader' #Set Download Position
print(f'start position {cd}')
print(f'Download Position : {dp}')
os.chdir(dp)
print(f'Now in {os.getcwd()}')
#Check 'Audio','Video',Channel' Folder Exists/If exists Retrun/Not exists Make that folder
root = Tk()
if os.path.isdir('Channel') == True :
    print('Channel Folder Already Exists')
else:
    os.mkdir('Channel')
def on_progress(stream, chunk, bytes_remaining):
    global filesize
    filesize = stream.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳  |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()
def walalaru():
    ChannelInput = txt.get()
    ch = Channel(ChannelInput)
    if os.path.isdir(f'Channel/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Already Exists')
    else:
        os.mkdir(f'Channel/{ch.channel_name}')
    if os.path.isdir(f'Channel/{ch.channel_name}/Audio') == True :
        print(f'Channel {ch.channel_name} Audio Folder Already Exists')
    else :
        os.mkdir(f'Channel/{ch.channel_name}/Audio')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'Channel/{ch.channel_name}/Audio')
    global counted
    counted = 0
    global fullcount
    fullcount = len(ch)
    threads = [ch.videos]
    for video in ch.videos:
        counted = counted + 1
        print(f'---{fullcount}/{counted}----------------------')
        t = threading.Thread(target=downloadvideo, args=(video,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print('finish')

def downloadvideo(video):
    if os.path.isfile(f'{video.title}.mp4') == False :
        print(f'{fullcount}/{counted}Video not Exists, Start Download {video.title}')
        video.streams.filter(only_audio=True).get_audio_only().download()
        video.bypass_age_gate = True
        video.register_on_progress_callback(on_progress)
        print(f'{fullcount}/{counted}Video Download Finished {video.title}')
    else:
        print(f'{fullcount}/{counted}Video Already Exists {video.title}')
#####
root.title("Youtube Downloader")
root.configure(background='#f2f2f2')
#####
#####
lbl = tkinter.Label(root, text="URL", font=("Arial Bold", 16))
lbl.pack()
txt = tkinter.Entry(root, width=50, font=("Arial Bold", 16))
txt.pack()
download = tkinter.Button(root, text="Download", command=walalaru, font=("Arial Bold", 16))
download.pack()
#########
root.mainloop()