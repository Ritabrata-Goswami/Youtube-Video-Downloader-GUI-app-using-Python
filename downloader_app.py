import sys

from PyQt5 import *
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

from pytube import YouTube


class youtube_downloader_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Downloader -by Ritabrata'
        self.left = 500
        self.top = 200
        self.width = 600
        self.height = 400
        self.create_qr_app_UI()

    def create_qr_app_UI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.header_one = QLabel(self)
        self.header_one.setText("Youtube Video Downloader")
        self.header_one.move(15, 5)
        self.header_one.resize(400, 70)
        self.header_one.setStyleSheet("font-size: 20pt; font-weight:bold; font-family:Arial;")

        self.instruction = QLabel(self)
        self.instruction.setText("Instruction:")
        self.instruction.move(15, 35)
        self.instruction.resize(400, 100)
        self.instruction.setStyleSheet("font-size: 11pt; color:red; font-family:Arial;")

        self.instruction_text = QLabel(self)
        self.instruction_text.setText("Copy the youtube video url from the youtube and paste that url below tab. Set the video stream rate in order to get the desired video resolution.\nFor example a youtube video url looks like:- https://www.youtube.com/watch?v=xt12Umk6Ry")
        self.instruction_text.move(90, 45)
        self.instruction_text.resize(1000, 100)
        self.instruction_text.setStyleSheet("font-size: 11pt; color:black; font-family:Arial;")

        self.label_1 = QLabel(self)
        self.label_1.setText("Enter Url:")
        self.label_1.move(15, 150)
        # self.label_1.resize(400, 10)
        self.label_1.setStyleSheet("font-size: 12pt; font-weight:bold; font-family:Arial;")

        self.textbox_1 = QLineEdit(self)
        self.textbox_1.move(95, 150)
        self.textbox_1.resize(400, 35)
        self.textbox_1.setPlaceholderText('http://www.youtube.com/watch?v=xt12Umk6Ry')
        self.textbox_1.setStyleSheet("font-size: 11pt;")

        self.label_2 = QLabel(self)
        self.label_2.setText("Select Stream:")
        self.label_2.move(15, 210)
        self.label_2.resize(200, 20)
        self.label_2.setStyleSheet("font-size: 12pt; font-weight:bold; font-family:Arial;")

        self.rate = QComboBox(self)
        self.rate.addItem('-select-')
        self.rate.addItem('144p')
        self.rate.addItem('240p')
        self.rate.addItem('360p')
        self.rate.addItem('480p')
        self.rate.addItem('720p')
        self.rate.move(130, 210)
        self.rate.setStyleSheet("font-size: 12pt;")
        self.rate.activated.connect(self.set_rate)

        self.dwl_button = QPushButton('Download', self)
        self.dwl_button.move(120,300)
        self.dwl_button.setStyleSheet("background:#00802b; color:#ffffff; font-size:15px;")
        self.dwl_button.clicked.connect(self.download_youtube)

        self.textbox_get_rate = QLineEdit(self)
        self.textbox_get_rate.move(150, 350)
        self.textbox_get_rate.resize(300, 35)
        self.textbox_get_rate.hide()
        

        self.show()

    def set_rate(self):
        rate_val = self.rate.currentText()
        self.textbox_get_rate.setText(str(rate_val))
        print(rate_val)
    
    def download_youtube(self):
        url_val = self.textbox_1.text()
        rate_val = self.textbox_get_rate.text()

        popup = QMessageBox()
        
        if url_val=="" or rate_val=="" or rate_val=="-select-":
            popup.setWindowTitle("Warning")
            popup.setIcon(QMessageBox.Warning)
            popup.setText("Field's Should Not Be Left Blank!")
            popup.setStyleSheet("font-size:13px;")
            popup.exec_()
        else:
            youtubeObject = YouTube(url_val) 
            youtubeObject = youtubeObject.streams.get_by_resolution(rate_val)
            try:
                youtubeObject.download()
            except Exception as e:
                popup.setWindowTitle("Error Information")
                popup.setIcon(QMessageBox.Information)
                popup.setText(str(e))
                popup.setStyleSheet("font-size:13px;")
                popup.exec_()
            
            popup.setWindowTitle("Success")
            popup.setText("Download Completed!")
            popup.setStyleSheet("font-size:13px;")
            popup.exec_()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = youtube_downloader_app()
    sys.exit(app.exec())