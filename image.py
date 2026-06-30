from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("image.ui",self)

        # define widgets
        self.button = self.findChild(QPushButton,"pushButton")
        self.label = self.findChild(QLabel, "label")

        # click button
        self.button.clicked.connect(self.clicker)



        # show the app
        self.show()

    def clicker(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*.);; PNG File (*.png);; JPEG Files (*.jpg)")

        # open the image
        self.pixmap = QPixmap(fname[0])
        # add pic to label
        self.label.setPixmap(self.pixmap)
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()