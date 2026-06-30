from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("dependentcombo.ui",self)


        # show the app
        self.show()
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()