from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QSlider
from PyQt5 import uic
from PyQt5 import QtCore
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("vslider.ui",self)
        self.setWindowTitle("Vertical Slider!")

        # define widgets
        self.slider = self.findChild(QSlider, "verticalSlider")
        self.label = self.findChild(QLabel, "label")

        # center the label
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # set slider properties
        self.slider.setMinimum(0)
        self.slider.setMaximum(50)
        #self.slider.setTickPosition(TicksLeft)
        #self.slider.setTickInterval(5)
        self.slider.setSingleStep(5)

        # move slider
        self.slider.valueChanged.connect(self.slideIt)


        # show the app
        self.show()

    def slideIt(self, value):
        self.label.setText(str(value))
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()