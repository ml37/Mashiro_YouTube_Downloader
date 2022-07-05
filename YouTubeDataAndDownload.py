from matplotlib.image import thumbnail
import pytube
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
import sys
from pytube import YouTube
from pytube import Channel

form_class = uic.loadUiType("analyzer.ui")[0]
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.progressBar.setValue(0)
        self.btn_load.clicked.connect(self.walalaru)
        self.btn_download.clicked.connect(self.download)
        self.lbl_len.setText("0")
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_changed)
    def download(self):
        print('download')
        print(streamhaschanged)
        streamhaschanged.download()

    def on_comboBox_changed(self):
        print('comboBox changed')
        print(self.comboBox.currentText())
        print(connecttitleandnum[self.comboBox.currentText()])
        stream = connecttitleandnum[self.comboBox.currentText()]
        print(stream.filter(progressive=True).order_by('resolution').desc().first())
        global streamhaschanged
        streamhaschanged = stream.filter(progressive=True).order_by('resolution').desc().first()
    def walalaru(self):
        global connect
        global connecttitleandnum
        global thumbnailurl
        connect = {'title': ''}
        connecttitleandnum = {'title': ''}
        self.comboBox.clear()
        ch = Channel('https://www.youtube.com/channel/UCAjWiWgGWg1ingZUoRLVgKw')
        print('=' * 50)
        print(len(ch))
        self.lbl_len.setText(str(len(ch)))
        length = len(ch)
        count = 0
        current = count/length
        percent = ('{0:.1f}').format(current*100)
        for video in ch.videos:
            count = count + 1
            connect[count] = video.streams
            connecttitleandnum[video.title] = video.streams
            thumbnailurl = video.thumbnail_url
            current = count/length
            percent = ('{0:.0f}').format(current*100)
            print(video.title)
            print(video)
            self.comboBox.addItem(video.title)
            self.progressBar.setValue(int(percent))
            print(f'current: {current}')
            print(f'percent: {percent}')
            print(f'count: {count}')
            print(f'length: {length}')
        print(connect)
        print('=' * 50)
        print(connecttitleandnum)
            
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
    sys.exit(0)