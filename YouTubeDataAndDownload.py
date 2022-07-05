import pytube
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from pytube import YouTube
from pytube import Channel
import urllib
import threading
import math

form_class = uic.loadUiType("analyzer.ui")[0]
global comboboxstillload
comboboxstillload = 1
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.btn_load.clicked.connect(self.comboboxload)
        self.btn_download.clicked.connect(self.download)
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_changed)
        self.lbl_len.setText("0")
    def download(self):
        print('download')
        for video in ch.videos:
            if video.title == self.comboBox.currentText():
                stream = video.streams.filter(progressive=True).order_by('resolution').desc().first()
                stream.download()
                print('download complete')
                self.progressBar.setValue(100)

    def on_comboBox_changed(self):
        print('comboBox changed')
        print(f'comboboxstillload : {comboboxstillload}')
        if comboboxstillload == 1:
            print('comboBox still load')
        elif comboboxstillload == 0:
            for video in ch.videos:
                if video.title == self.comboBox.currentText():
                    thumbnailurl = video.thumbnail_url
                    print(thumbnailurl)
                    imageFromWeb = urllib.request.urlopen(thumbnailurl).read()
                    self.qPixmapWebVar = QPixmap()
                    self.qPixmapWebVar.loadFromData(imageFromWeb)
                    self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(480)
                    self.lbl_picture.setPixmap(self.qPixmapWebVar)
                    
                    self.lbl_author.setText(f'Author : {video.author}')
                    #self.lbl_title.setText(f'Title : {video.title}')
                    self.lbl_view.setText(f'Views : {video.views}')
                    self.lbl_length.setText(f'Length : {video.length//60}:{int(math.fmod(video.length,60))}')
                    #self.lbl_resolution.setText(f'Resolution : {video.resolution}')
                    #self.lbl_filesize.setText(f'File Size : {round((video.filesize)*0.000001,2)}MB')
                    #self.lbl_mime.setText(f'Type : {video.mime_type}')
    '''def walalaru(self):
        global connecttitleandnum
        global thumbnailurl
        connecttitleandnum = {'title': ''}
        self.comboBox.clear()
        ch = Channel('https://www.youtube.com/channel/UCAjWiWgGWg1ingZUoRLVgKw')
        self.lbl_len.setText(str(len(ch)))
        length = len(ch)
        count = 0
        current = count/length
        percent = ('{0:.1f}').format(current*100)
        for video in ch.videos:
            count = count + 1
            connecttitleandnum[video.title] = video.streams
            thumbnailurl = video.thumbnail_url
            current = count/length
            percent = ('{0:.0f}').format(current*100)
            self.comboBox.addItem(video.title)
            self.progressBar.setValue(int(percent))'''
    
    def comboboxload(self):
        global ch
        url=self.txt.text()
        self.comboBox.clear()
        ch = Channel(url)
        print('load')
        print(len(ch))
        self.lbl_len.setText(str(len(ch)))
        length = len(ch)
        count = 0
        threads = [ch.videos]
        for video in ch.videos:
            count = count + 1
            def walalaru(self):
                print([count])
                self.comboBox.addItem(video.title)
            t = threading.Thread(target=walalaru(self), args=(video,))
            t.start()
            threads.append(t)
        print('load finish')
        global comboboxstillload
        comboboxstillload = 0
        print(comboboxstillload)

    
            
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit(0)