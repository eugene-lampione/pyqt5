from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("load.ui",self)

        # define our widgets
        self.label = self.findChild(QLabel, "label")
        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.button = self.findChild(QPushButton, "pushButton")
        self.clearButton = self.findChild(QPushButton, "pushButton_2")

        # do something
        self.button.clicked.connect(self.clicker)
        self.clearButton.clicked.connect(self.clearer)

        # show the app
        self.show()

    def clicker(self):
        self.label.setText(f'Hello there, {self.textedit.toPlainText()}')
        self.textedit.setPlainText("")

    def clearer(self):
        self.textedit.setPlainText("")
        self.label.setText("Enter you name here: ")

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()