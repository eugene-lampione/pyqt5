from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("hidewidgets.ui",self)
        self.setWindowTitle("Hide/Unhide Widgets!")

        # define our widgets
        self.edit = self.findChild(QLineEdit,"lineEdit")
        self.button = self.findChild(QPushButton,"pushButton")

        # click the button
        self.button.clicked.connect(self.hideunhide)


        # show the app
        self.show()

        # keep track of hidden state
        self.hidden = False

    def hideunhide(self):
        if self.hidden:
            self.edit.show()
            self.hidden = False 
        else:
            self.edit.hide()
            self.hidden = True

        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()