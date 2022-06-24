from pytube import YouTube
from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType('basic.ui')[0]
RB_mimi_type = 'mp4'
AudioOnly = 'off'
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Btn_Download.clicked.connect(self.Btn_Download_clicked)
        self.RB_WebM.clicked.connect(self.RB_WebM_clicked)
        self.RB_MP4.clicked.connect(self.RB_MP4_clicked)
        self.CBox_AudioOnly.stateChanged.connect(self.CBox_AudioOnly_Changed)
        self.ComBox_Resolution.currentIndexChanged.connect(self.ComBox_Resolution_Changed)

    def Btn_Download_clicked (self):
        print('----------------------------------------------------')
        print(RB_mimi_type)
        print(f'Audio Only : {AudioOnly}')
        print(self.ComBox_Resolution.currentText())

    def RB_WebM_clicked (self):
        print('WebM')
        RB_mimi_type = 'WebM'
    def RB_MP4_clicked (self):
        print('MP4')
        RB_mimi_type = 'MP4'
    def CBox_AudioOnly_Changed (self):
        if self.CBox_AudioOnly.isChecked() == True:
            print('Audio Only Turned on')
            AudioOnly = 'on'
        elif self.CBox_AudioOnly.isChecked() == False:
            print('Audio Only Turned off')
            AudioOnly = 'off'
    def ComBox_Resolution_Changed (self):
        print(self.ComBox_Resolution.currentText())

if __name__ =='__main__':
        app = QApplication(sys.argv)
        mywindow = MyWindow()
        mywindow.show()
        app.exec_()
