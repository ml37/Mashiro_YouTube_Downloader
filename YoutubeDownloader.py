#YouTube Downloader made with Github Copilot
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
import asyncio
#Save Startposition in 'cd'
cd=os.getcwd()
dp='D:\Download\YoutubeDownloader' #Set Download Position
print(f'start position {cd}')
print(f'Download Position : {dp}')
os.chdir(dp)
print(f'Now in {os.getcwd()}')
#Check 'Audio','Video',Channel' Folder Exists/If exists Retrun/Not exists Make that folder
if os.path.isdir('Audio') == True :
    print('Audio Folder Already Exists')
else:
    os.mkdir('Audio')
if os.path.isdir('Video') == True :
    print('Video Folder Already Exists')
else:
    os.mkdir('Video')
if os.path.isdir('Channel') == True :
    print('Channel Folder Already Exists')
else:
    os.mkdir('Channel')
if os.path.isdir('Playlist') == True :
    print('Playlist Folder Already Exists')
else:
    os.mkdir('Playlist')
#Set tkinter.Tk() as root
root = tkinter.Tk()

#progressbar On CLI 
def on_progress(stream, chunk, bytes_remaining):
    global filesize
    filesize = stream.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳  |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()
#progressbar on list
def on_progress_list():
    current_list = (count)/(fullcount)
    percent_list = ('{0:.1f}').format(current_list*100)
    progress_list = int(50*current_list)
    status_list = '█' * progress_list + '-' * (50 - progress_list)
    sys.stdout.write(' ↳  |{bar}| {percent}%\r'.format(bar=status_list, percent=percent_list))
    sys.stdout.flush()
    
    
#Single, Audio only download
def AudioClick():
    os.chdir(f'Audio')
    print("Audio Download Button Clicked") 
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(only_audio=True).get_audio_only()
    yt.bypass_age_gate = True
    yt.register_on_progress_callback(on_progress)
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Audio/{yt.title}.mp4')
    print("Download Complete")
    os.chdir(dp)
#Single, Video Download
def VideoClick():
    os.chdir(f'Video')
    print("Video Download Button Clicked")
    urlInput = txt.get()
    print(urlInput)
    yt = YouTube(urlInput)
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
    yt.bypass_age_gate = True
    yt.register_on_progress_callback(on_progress)
    stream.download()
    shutil.move(f'{yt.title}.mp4', f'Video/{yt.title}.mp4')
    print("Download Complete")
    os.chdir(dp)
#All of Channel, Video Download
def chVideoClick():
    print('Download Channel Video')
    ChannelInput = txt.get()
    ch = Channel(ChannelInput)
    print(f'==========Downloading videos by: {ch.channel_name}==========')
    print(f'Channel Video List//Total Video : {len(ch)}')
    #print(ch) #for Debug
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
    global count
    count = 0
    global fullcount
    fullcount = len(ch)
    for video in ch.videos:
        count = count + 1
        print(f'---{len(ch)}/{count}-----Title:{video.title}-----------------')
        if os.path.isfile(f'{video.title}.mp4') == False :
            print(f'Video {video.title} not Exists, Start Download')
            video.streams.filter(progressive=True).order_by('resolution').desc().first().download()
            video.bypass_age_gate = True
            video.register_on_progress_callback(on_progress)
            print(f'Video {video.title} Download Finished')
        else:
            print(f'Video {video.title} Already Exists')
    print(f'==========Channel Video Download({len(ch)}) Complete==========')
    os.chdir(dp)
#All of Channel, Audio only Download
def chAudioClick():
    print('Download Channel Audio')
    ChannelAudioInput = txt.get()
    ch = Channel(ChannelAudioInput)
    print(f'==========Downloading Audio by: {ch.channel_name}==========')
    print('Channel Video List//Total Video : '+str(len(ch)))
    #print(ch) #for Debug
    if os.path.isdir(f'Channel/{ch.channel_name}') == True :
        print(f'Channel {ch.channel_name} Folder Already Exists')
    else:
        os.mkdir(f'Channel/{ch.channel_name}')
    if os.path.isdir(f'Channel/{ch.channel_name}/Audio') == True :
        print(f'Channel {ch.channel_name} Audio Folder Already Exists')
    else :
        os.mkdir(f'Channel/{ch.channel_name}/Audio')
    print('----')
    print('Channel Audio Download Start')
    os.chdir(f'Channel/{ch.channel_name}/Audio')
    global count
    count = 0
    global fullcount
    fullcount = len(ch)
    for video in ch.videos:
        count = count + 1
        print(f'---{len(ch)}/{count}-----Title:{video.title}-----------------')
        if os.path.isfile(f'{video.title}.mp4') == False :
            print(f'Audio {video.title} not Exists, Start Download')
            video.streams.filter(only_audio=True).get_audio_only().download()
            video.bypass_age_gate = True
            video.register_on_progress_callback(on_progress)
            print(f'Audio "{video.title}" Download Finished')
        else:
            print(f'Audio "{video.title}" Already Exists')
    print(f'==========Channel Audio Download({len(ch)}) Complete==========')
    os.chdir(dp)
def playlistVideoClick():
    print('Download Playlist Video')
    playlistInput = txt.get()
    pl = Playlist(playlistInput)
    print(f'==========Downloading videos by: {pl.title}==========')
    print(f'Playlist Video List//Total Video : {len(pl)}')
    #print(pl) #for Debug
    if os.path.isdir(f'playlist/{pl.title}') == True :
        print(f'Playlist {pl.title} Folder Already Exists')
    else:
        os.mkdir(f'playlist/{pl.title}')
    if os.path.isdir(f'playlist/{pl.title}/Video') == True :
        print(f'Playlist {pl.title} Video Folder Already Exists')
    else :
        os.mkdir(f'playlist/{pl.title}/Video')
    print('----')
    print('Playlist Video Download Start')
    os.chdir(f'playlist/{pl.title}/Video')
    global count
    count = 0
    global fullcount
    fullcount = len(ch)
    for video in pl.videos:
        print(f'---{len(pl)}/{count}-----Title:{video.title}-----------------')
        if os.path.isfile(f'{video.title}.mp4') == False :
            print(f'Video {video.title} not Exists, Start Download')
            video.streams.filter(progressive=True).order_by('resolution').desc().first().download()
            video.bypass_age_gate = True
            video.register_on_progress_callback(on_progress)
            print(f'Video {video.title} Download Finished')
        else:
            print(f'Video {video.title} Already Exists')
    print(f'==========Playlist Video Download({len(pl)}) Complete==========')
    os.chdir(dp)
def playlistAudioClick():
    print('Download Playlist Audio')
    playlistInput = txt.get()
    pl = Playlist(playlistInput)
    print(f'==========Downloading Audio by: {pl.title}==========')
    print('Playlist Video List//Total Video : '+str(len(pl)))
    #print(pl) #for Debug
    if os.path.isdir(f'playlist/{pl.title}') == True :
        print(f'Playlist {pl.title} Folder Already Exists')
    else:
        os.mkdir(f'playlist/{pl.title}')
    if os.path.isdir(f'playlist/{pl.title}/Audio') == True :
        print(f'Playlist {pl.title} Audio Folder Already Exists')
    else :
        os.mkdir(f'playlist/{pl.title}/Audio')
    print('----')
    print('Playlist Audio Download Start')
    os.chdir(f'playlist/{pl.title}/Audio')
    global count
    count = 0
    global fullcount
    fullcount = len(ch)
    for video in pl.videos:
        count = count + 1
        print(f'---{len(pl)}/{count}-----Title:{video.title}-----------------')
        if os.path.isfile(f'{video.title}.mp4') == False :
            print(f'Audio {video.title} not Exists, Start Download')
            video.streams.filter(only_audio=True).get_audio_only().download()
            video.bypass_age_gate = True
            video.register_on_progress_callback(on_progress)
            print(f'Audio "{video.title}" Download Finished')
        else:
            print(f'Audio "{video.title}" Already Exists')
    print(f'==========Playlist Audio Download({len(pl)}) Complete==========')
    os.chdir(dp)
#Radio Button Interction print(For Debug)
def selSingle():
    print('select Single')
def selChannel():
    print('select Channel')
def selAudio():
    print('select Audio')
def selVideo():
    print('select Video')
def selPlaylist():
    print('select Playlist')
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
    elif var.get() == 3:
        print('Playlist Video')
        if VorA.get() == 1:
            print('Audio')
            playlistAudioClick()
        elif VorA.get() == 2:
            print('Video')
            playlistVideoClick()
    else:
        print('Nothing Selected')
        return
def standby():
    print('Standby for next Download')
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
frame4 = tkinter.Frame(root, relief="solid", bd=2)
frame1.pack(side="left", fill="both")
frame2.pack(side="left", fill="both")
frame3.pack(side="left", fill="both")
frame4.pack(side="left", fill="both")
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
R5 = tkinter.Radiobutton(frame2, text="Playlist", variable=var, value=3, command=selPlaylist)
R5.pack(side=LEFT)
#####
R3 = tkinter.Radiobutton(frame3, text="Audio", variable=VorA, value=1, command=selAudio)
R3.pack(side=LEFT)
R4 = tkinter.Radiobutton(frame3, text="Video", variable=VorA, value=2, command=selVideo)
R4.pack(side=LEFT)
#########
root.mainloop()