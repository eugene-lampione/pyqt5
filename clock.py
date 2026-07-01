from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from PyQt5 import uic
import sys
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("clock.ui",self)

        # define our widget
        self.lcd = self.findChild(QLCDNumber, 'lcdNumber')

        # create atimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.clocker)

        # start the time and update everysecond
        self.timer.start(1000)

        # call the clocker function
        self.clocker()


        # show the app
        self.show()

    def clocker(self):
        # get the time
        time = datetime.now()
        formattedTime = time.strftime("%I:%M:%S %p")

        # set number of digits
        self.lcd.setDigitCount(12)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(formattedTime)
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()