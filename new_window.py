from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QMdiArea,QMdiSubWindow, QTextEdit
from PyQt5 import uic
import sys 

class UI(QMainWindow):
    count = 0

    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("new_window.ui",self)

        # define out widget
        self.mdi = self.findChild(QMdiArea,"mdiArea")
        self.button = self.findChild(QPushButton,"pushButton")

        # click the button
        self.button.clicked.connect(self.addWindow)


        # show the app
        self.show()

    def addWindow(self):
        UI.count = UI.count + 1

        # create subwindow
        sub = QMdiSubWindow()
        
        # do stuff in window
        sub.setWidget(QTextEdit())

        # set the title bar
        sub.setWindowTitle("Sub Window " + str(UI.count))

        # add sub window into MDI area
        self.mdi.addSubWindow(sub)

        # show the new sub window
        sub.show()

        # position the sub windows
        # tile them
        #self.mdi.tileSubWindows()

        # cascade them
        self.mdi.cascadeSubWindows()

        # self.mdi.closeActiveSubWindow()
        # self.mdi.removeActiveSubWindow()
        # self.mdi.subWindowList()

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()