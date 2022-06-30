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
def walalaru():
    ChannelInput = txt.get()
    ch = Channel(ChannelInput)
    if os.path.isdir(f'Channel/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Already Exists')
    else:
        os.mkdir(f'Channel/{ch.channel_name}')
    if os.path.isdir(f'Channel/{ch.channel_name}/Video') == True :
        print(f'Channel {ch.channel_name} Video Folder Already Exists')
    else :
        os.mkdir(f'Channel/{ch.channel_name}/Video')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'Channel/{ch.channel_name}/Video')
    global counted
    counted = 0
    global fullcount
    fullcount = len(ch)
    threads = [ch.videos]
    for video in ch.videos:
        counted = counted + 1
        print(f'---{len(ch)}/{count}----------------------')
        t = threading.Thread(target=downloadvideo, args=(video,))
        t.start()
        threads.append(t)
        time.sleep(3)
    for t in threads:
        t.join()
    print('finish')

def downloadvideo(video):
    if os.path.isfile(f'{video.title}.mp4') == False :
        print(f'Video not Exists, Start Download {video.title}')
        video.streams.filter(progressive=True).order_by('resolution').desc().first().download()
        video.bypass_age_gate = True
        print(f'Video Download Finished {video.title}')
    else:
        print(f'Video Already Exists {video.title}')
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