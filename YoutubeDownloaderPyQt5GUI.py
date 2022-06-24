import sys
from tkinter.ttk import Progressbar
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from pytube import YouTube
from pytube import Channel
import os
from os import path
import shutil
from re import T
import math
#Save Startposition in 'cd'
cd=os.getcwd()

#url='https://www.youtube.com/watch?v=BivuVeVVgF8&list=RDBivuVeVVgF8&start_radio=1&ab_channel=MBCkpop' #For test


#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.

global self


form_class = uic.loadUiType("Downloader.ui")[0]
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
    
        self.btn_ok.clicked.connect(self.ok)
        self.btn_download.clicked.connect(self.download)
        self.btn_download_all.clicked.connect(self.download_all)

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.timer = QBasicTimer()
        print(self.pbar.value())

    
    def ok(self) :
        #사용자가 입력한 값을 읽어오기
        
        print(self.txt_url.text())
        global url, yt, stream, ch
        url=self.txt_url.text()
        yt=YouTube(url)
        self.lbl_author.setText(f'Author : {yt.author}')
        self.lbl_title.setText(f'Title : {yt.title}')
        self.lbl_view.setText(f'Views : {yt.views}')
        self.lbl_length.setText(f'Length : {yt.length//60}:{int(math.fmod(yt.length,60))}')
        stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
        self.lbl_resolution.setText(f'Resolution : {stream.resolution}')
        self.lbl_filesize.setText(f'File Size : {round((stream.filesize)*0.000001,2)}MB')
        self.lbl_mime.setText(f'Type : {stream.mime_type}')
        ch=Channel(yt.channel_url)
        print(yt.captions)
        print(yt.caption_tracks)
        urlString = yt.thumbnail_url
        imageFromWeb = urllib.request.urlopen(urlString).read()
        self.qPixmapWebVar = QPixmap()
        self.qPixmapWebVar.loadFromData(imageFromWeb)
        self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(480)
        self.lbl_picture.setPixmap(self.qPixmapWebVar)
    def download(self, percentage_of_completion) :
        print('walalalru')
        print(stream)
        #self.progressBar.setValue(percentage_of_completion)
        stream.download()
    def download_all(self) :
        print('walalalru')
        print(stream)
        #syt.register_on_progress_callback(myprogressbar)
        stream.registeron_progress_callback(myprogressbar)
        stream.download()
    def ytprobar(self, stream, chunk, bytes_remaining):
        print('walalalru')
        print(stream)
        print(chunk)

def myprogressbar(stream, chunk, bytes_remaining):
    print('downloadsss')
    total_size = stream.filesize
    bytes_downloaded = (total_size - bytes_remaining)
    bytes_remaining_MB = round(bytes_remaining*0.000001,1)
    done_size = round((total_size - bytes_remaining)*0.000001,1)
    global percentage_of_completion
    percentage_of_completion = round(bytes_downloaded / total_size * 100, 1)
    #print(f'{percentage_of_completion}%, {done_size}MB/{bytes_remaining_MB}MB')
    global progress
    progress = (f'{percentage_of_completion}%, {done_size}MB/{bytes_remaining_MB}MB')
    print(progress)
    self.progressBar.setValue(percentage_of_completion)
        
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()