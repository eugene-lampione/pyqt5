from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("color.ui",self)

        # add menu triggers
        self.actionBlack.triggered.connect(lambda: self.change("black"))
        self.actionWhite.triggered.connect(lambda: self.change("white"))
        self.actionRed.triggered.connect(lambda: self.change("red"))
        self.actionBlue.triggered.connect(lambda: self.change("blue"))
        self.actionGreen.triggered.connect(lambda: self.change("green"))
        self.actionYellow.triggered.connect(lambda: self.change("yellow"))
        self.actionOrange.triggered.connect(lambda: self.change("orange"))

        # show the app
        self.show()

    def change(self, color):
        # change the bg color
        self.setStyleSheet(f"background-color: {color};")
        # change the title
        self. setWindowTitle(f'You changed the color to: {color}')
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()