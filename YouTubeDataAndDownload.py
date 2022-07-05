import pytube
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from pytube import YouTube
from pytube import Channel
import urllib

form_class = uic.loadUiType("analyzer.ui")[0]
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
        for video in ch.videos:
            if video.title == self.comboBox.currentText():
                thumbnailurl = video.thumbnail_url
                print(thumbnailurl)
                imageFromWeb = urllib.request.urlopen(thumbnailurl).read()
                self.qPixmapWebVar = QPixmap()
                self.qPixmapWebVar.loadFromData(imageFromWeb)
                self.qPixmapWebVar = self.qPixmapWebVar.scaledToWidth(480)
                self.lbl_picture.setPixmap(self.qPixmapWebVar)
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
        self.comboBox.clear()
        ch = Channel('https://www.youtube.com/channel/UCAjWiWgGWg1ingZUoRLVgKw')
        self.lbl_len.setText(str(len(ch)))
        length = len(ch)
        count = 0
        for video in ch.videos:
            count = count + 1
            self.comboBox.addItem(video.title)
            
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit(0)