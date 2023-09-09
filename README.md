# Youtube-Video-Downloader-GUI-app-using-Python
To build such app you have to install pytube module using
```
pip install pytube
```
hit in cmd. 
Import this module as ```from pytube import YouTube```.
```
from PyQt5 import *
from PyQt5.QtGui import QGuiApplication
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtQuick import QQuickWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
```
Import all this pyqt5 module that helps to build your app.
Declare a class and pass a argument name QMainWindow which actually create the GUI app.
Initiate all the properties under it such as title, width, height and the method which is under the class of 'youtube_downloader_app'. 
```
self.create_qr_app_UI()
```
Here create_qr_app_UI() is a method that is under the class and under which all the logics will be written.

QLabel(self) helps to write any text.
QLineEdit(self) helps to create textbox similar to <input type="text"/> we do in HTML.
QComboBox(self) helps to create dropdown box similar to <select><option/>....<option/></select> in HTML.
QPushButton('Download', self) is create button.
setStyleSheet() is use to styling the app. The syntax is almost similar as CSS we write incase of building web app.

### Finally downloading youtube video

youtubeObject = YouTube(video_link)     
This line Creating a object using YouTube() method and video url passing inside that method. So that it create a object of that video and later we can access that video information using inbuild property of the pytube module. 

youtubeObject = youtubeObject.streams.get_by_resolution(rate_val)
Many solutions shows ```streams.get_highest_resolution()```. get_highest_resolution() is actually download that video with heighest possible data rate without allowing any control of it. 
But get_by_resolution(rate_val) does allow you to select your won data rate you want to allow. Such as 144p, 360p, 720p etc.
At last youtubeObject.download() that downloads the video.

If download successful it pops up a message.
