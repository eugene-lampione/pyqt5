from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QCalendarWidget
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("calendar.ui",self)

        # define our widget
        self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
        self.label = self.findChild(QLabel, "label")

        # connect calendat to function
        self.calendar.selectionChanged.connect(self.grabDate)

        # show the app
        self.show()

    def grabDate(self):
        dateSelected = self.calendar.selectedDate()

        # put date on label
        self.label.setText(str(dateSelected.toString()))
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()