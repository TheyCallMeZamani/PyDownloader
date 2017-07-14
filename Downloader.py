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
        QDialog.__init__(self)   # initializing the QDialog
        layout = QVBoxLayout()  # the main Layout
        self.setGeometry(300,100,300,300) # x,y Width and Height

# defining Widgets

        self.url = QLineEdit()     # for the URl Box
        self.save_location = QLineEdit()     #Address of saving the file
        self.progress = QProgressBar()
        self.downloadBtn = QPushButton("Download", self)  # Download Button
        self.downloadBtn.clicked.connect(self.download)  # Conncet Button to Download Event
        self.browse = QPushButton("Browse")
        self.browse.clicked.connect(self.saveFileDialog)
        self.urlparse = QLineEdit()
        self.sizelbl = QLabel()
        self.parserbtn = QPushButton("Parse", self)  # Parser Button
        self.parserbtn.clicked.connect(self.parsing)
        self.urlparse.setPlaceholderText("Insert Link To parse")
        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File Save Location")
        self.txtbox = QTextBrowser()

# Adding the items to the layout

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)  # Horizontally Aligned Center

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.browse)
        layout.addWidget(self.progress)
        layout.addWidget(self.downloadBtn)
        layout.addWidget(self.urlparse)
        layout.addWidget(self.parserbtn)
        layout.addWidget(self.txtbox)
        layout.addWidget(self.sizelbl)



# Add the layout to the QDialog

        self.setLayout(layout)
        self.setWindowTitle("Safahan Downloader Project")
        self.setFocus()

# Methods

    def parsing(self):
        url = self.urlparse.text()
        content = urlopen(url).read()
        soup = BeautifulSoup(content, 'html.parser')
        self.txtbox.setHtml(str(soup.find_all('a')))
        print
        soup.prettify()
#        url = self.url.text()
#        soup = BeautifulSoup(self.download, 'html.parser')
#        soup.findAll('a', attrs={'href': re.compile("^http://")})
#        for link in soup.find_all('a'):
#            self.txtbox.setHtml(str(link.get('href')))



    #def browse_file(self):
    #     save_file = QFileDialog.getSaveFileName(self, caption="Save File As", directory=".", filter="All Files (*.txt)")
    #     self.save_location.setText(QDir.toNativeSeparators(save_file))

    def saveFileDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "", "All Files (*);;Text Files (*.txt)", options=options)
        self.save_location.setText(fileName)

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

#get the size of file before downloading
        site = urlopen(url)
        meta = site.info()['Content-Length'] # or for the type of file ==> [Content-Type]
        self.sizelbl.setText("Size: " + str("{0:.2f}".format(int(meta)/1024) + "KB"))
#another ways to calculate the size of file
        #f = urlopen(self.url)
        #fsize =f.headers["Content-Length"] #len(f.read())
        #self.sizelbl.setText(int(fsize)/1024)
        #self.sizelbl.setText(str("{0:.2f}".format(int(fsize)/1024)+ "KB"))

# Exception Handler for URL
        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The Download Failed")
            return

        QMessageBox.information(self, "information", "The Download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")


    def report(self,blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0 :
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))

app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()