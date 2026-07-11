from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("bindtext.ui",self)
        self.setWindowTitle("Text Binding!")

        # define our widgets
        self.label = self.findChild(QLabel,"label")
        self.edit = self.findChild(QLineEdit, "lineEdit")

        # hit the enter button
        self.edit.editingFinished.connect(self.hitEnter)

        # on typing
        self.edit.textChanged.connect(self.changeText)


        # show the app
        self.show()

    def hitEnter(self):
        self.label.setText(self.edit.text())

    def changeText(self):
        self.label.setText(self.edit.text())
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()