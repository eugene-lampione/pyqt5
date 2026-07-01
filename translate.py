from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QComboBox, QMessageBox
from PyQt5 import uic
import sys
import googletrans
import textblob

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("translate.ui",self)
        self.setWindowTitle("Translator App!")

        # define our widgets
        


        # show the app
        self.show()
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()