from bs4 import BeautifulSoup
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import urllib.request
from urllib.request import urlopen
from interface import Ui_MainWindow
import re




class Downloader(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

# defining Widgets

        self.url = QLineEdit()     # for the URl Box
        self.save_location = QLineEdit()     #Address of saving the file
        self.progress = QProgressBar()
        self.downloadBtn = QPushButton("Download", self)  # Download Button
#        self.downloadBtn.clicked.connect(self.download)  # Conncet Button to Download Event
        self.browse = QPushButton("Browse")
#        self.browse.clicked.connect(self.saveFileDialog)
        self.urlparse = QLineEdit()
        self.sizelbl = QLabel()
        self.parserbtn = QPushButton("Parse", self)  # Parser Button
#        self.parserbtn.clicked.connect(self.parsing)
        self.urlparse.setPlaceholderText("Insert Link To parse")
        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File Save Location")
        self.txtbox = QTextBrowser()



app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()