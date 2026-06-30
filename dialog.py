from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QFileDialog
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("dialog.ui",self)

        # define our widget
        self.button = self.findChild(QPushButton,"pushButton")
        self.label = self.findChild(QLabel,"label")

        self.button.clicked.connect(self.clicker)


        # show the app
        self.show()

    def clicker(self):
        #self.label.setText("You clicked the button")
        # Open file dialog
        fname = QFileDialog.getOpenFileName(self,"Open File","Users\\Downloads\\","All Files (*);;Python Files(*.py);;PNG Files (*.png)")

        # output file name to screen
        if fname:
            self.label.setText(fname[0])
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()