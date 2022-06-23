#YouTube Downloader made with Github Copilot
from pytube import YouTube
from pytube import Channel
import os
from os import path
import shutil
from re import T
import tkinter
from tkinter import *
from tkinter import ttk
#Save Startposition in 'cd'
cd =os.getcwd()
print(f'start position {cd}')
#Check 'Audio','Video',Channel' Folder Exists/If exists Retrun/Not exists Make that folder
if os.path.isdir('Audio') == True :
    print('Audio Folder Already Exists')
else:
    os.mkdir('Audio')
if os.path.isdir('Video') == True :
    print('Video Folder Already Exists')
else:
    os.mkdir('Video')
if os.path.isdir('channel') == True :
    print('channel Folder Already Exists')
else:
    os.mkdir('channel')
#Set tkinter.Tk() as root
root = tkinter.Tk()
#Single, Audio only download
def AudioClick():
    print("Audio Download Button Clicked") 
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(only_audio=True).get_audio_only()
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Audio/{yt.title}.mp4')
    print("Download Complete")
#Single, Video Download
def VideoClick():
    print("Video Download Button Clicked")
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Video/{yt.title}.mp4')
    print("Download Complete")
#All of Channel, Video Download
def chVideoClick():
    print('Channel Download Button Clicked')
    channelInput = txt.get()
    ch = Channel(channelInput)
    print(f'Downloading videos by: {ch.channel_name}')
    print('Channel Video List')
    print(ch)
    if os.path.isdir(f'channel/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Exists')
    else:
        os.mkdir(f'channel/{ch.channel_name}')
    if os.path.isdir(f'channel/{ch.channel_name}/Video') == True :
        print(f'Channel {ch.channel_name} Video Folder Exists')
    else :
        os.mkdir(f'channel/{ch.channel_name}/Video')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'channel/{ch.channel_name}/Video')
    for video in ch.videos:
        print('-------')
        print(video.title)
        if os.path.isfile(f'{video.title}.mp4') == False :
            print(f'Video {video.title} not Exists')
            video.streams.filter(progressive=True).order_by('resolution').desc().first().download()
            print(f'Video {video.title} Downloaded')
        else:
            print(f'Video {video.title} Exists')
    print('Channel Video Download Complete')
    os.chdir(cd)
#All of Channel, Audio only Download
def chAudioClick():
    print('Channel Audio Download Button Clicked')
    channelAudioInput = txt.get()
    ch = Channel(channelAudioInput)
    print(f'Downloading videos by: {ch.channel_name}')
    print('Channel Video List')
    print(ch)
    if os.path.isdir(f'channel/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Exists')
    else:
        os.mkdir(f'channel/{ch.channel_name}')
    if os.path.isdir(f'channel/{ch.channel_name}/Audio') == True :
        print(f'Channel {ch.channel_name} Audio Folder Exists')
    else :
        os.mkdir(f'channel/{ch.channel_name}/Audio')
    print('----')
    print('Channel Video Download Start')
    os.chdir(f'channel/{ch.channel_name}/Audio')
    for video in ch.videos:
        print('-------')
        print(video.title)
        if os.path.isfile(f'{video.title}.mp4') == False :
            print(f'Audio {video.title} not Exists')
            video.streams.filter(only_audio=True).get_audio_only().download()
            print(f'Audio {video.title} Downloaded')
        else:
            print(f'Audio {video.title} Already Exists')
    os.chdir(cd)
    print('Channel Audio Download Complete')
#Radio Button Interction print(For Debug)
def selSingle():
    print('select Single')
def selChannel():
    print('select Channel')
def selAudio():
    print('select Audio')
def selVideo():
    print('select Video')
#If Download button clicked, Check var(Video or Audio), VorA(Single or Channel)
def DownloadClick():
    if var.get() == 1:
        print('Single Video')
        if VorA.get() == 1:
            print('Audio')
            AudioClick()
        elif VorA.get() == 2:
            print('Video')
            VideoClick()
    elif var.get() == 2:
        print('Channel Video')
        if VorA.get() == 1:
            print('Audio')
            chAudioClick()
        elif VorA.get() == 2:
            print('Video')
            chVideoClick()
    else:
        print('Nothing Selected')
        return
#tkinter GUI set
var = IntVar()
VorA = IntVar()
#####
root.title("Youtube Downloader")
root.configure(background='#f2f2f2')
#####
frame1 = tkinter.Frame(root, relief="solid", bd=2)
frame2 = tkinter.Frame(root, relief="solid", bd=2)
frame3 = tkinter.Frame(root, relief="solid", bd=2)
frame1.pack(side="left", fill="both")
frame2.pack(side="left", fill="both")
frame3.pack(side="left", fill="both")
#####
lbl = tkinter.Label(frame1, text="URL", font=("Arial Bold", 16))
lbl.pack(side="right")
txt = tkinter.Entry(frame1, width=50, font=("Arial Bold", 16))
txt.pack(side="right")
download = tkinter.Button(frame1, text="Download", command=DownloadClick, font=("Arial Bold", 16))
download.pack(side="right")
#####
R1 = tkinter.Radiobutton(frame2, text="Single", variable=var, value=1, command=selSingle)
R1.pack(side=LEFT)
R2 = tkinter.Radiobutton(frame2, text="Channel", variable=var, value=2, command=selChannel)
R2.pack(side=LEFT)
#####
R3 = tkinter.Radiobutton(frame3, text="Audio", variable=VorA, value=1, command=selAudio)
R3.pack(side=LEFT)
R4 = tkinter.Radiobutton(frame3, text="Video", variable=VorA, value=2, command=selVideo)
R4.pack(side=LEFT)
#########
root.mainloop()