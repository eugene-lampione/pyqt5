from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("dependentcombo.ui",self)

        # define widgets
        self.combo1 = self.findChild(QComboBox,"comboBox")
        self.combo2 = self.findChild(QComboBox,"comboBox_2")
        self.label = self.findChild(QLabel,"label")

        # add items to the combo boxes
        self.combo1.addItem("Male",["John","Wes","Dan"])
        self.combo1.addItem("Female",["April","Steph","Beth"])
        
        # click the first dropdown
        self.combo1.activated.connect(self.clicker)
        self.combo2.activated.connect(self.clicker2)


        # show the app
        self.show()

    def clicker(self, index):
        # clear the  second box
        self.combo2.clear()

        # do the dependent thing
        self.combo2.addItems(self.combo1.itemData(index))

    def clicker2(self):
        self.label.setText(f'You Picked: {self.combo2.currentText()} - {self.combo1.currentText()}')
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()