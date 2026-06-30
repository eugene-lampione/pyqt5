from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton
from PyQt5 import uic
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("tic-tac-toe.ui",self)

        # define counter to keep track of whos turn
        self.counter = 0

        #define widgets
        self.button1 = self.findChild(QPushButton, "pushButton_1")
        self.button2 = self.findChild(QPushButton, "pushButton_2")
        self.button3 = self.findChild(QPushButton, "pushButton_3")
        self.button4 = self.findChild(QPushButton, "pushButton_4")
        self.button5 = self.findChild(QPushButton, "pushButton_5")
        self.button6 = self.findChild(QPushButton, "pushButton_6")
        self.button7 = self.findChild(QPushButton, "pushButton_7")
        self.button8 = self.findChild(QPushButton, "pushButton_8")
        self.button9 = self.findChild(QPushButton, "pushButton_9")
        self.button10 = self.findChild(QPushButton, "pushButton_10")
        self.label = self.findChild(QLabel,"label")

        # click the button
        self.button1.clicked.connect(lambda:self.clicker(self.button1))
        self.button2.clicked.connect(lambda:self.clicker(self.button2))
        self.button3.clicked.connect(lambda:self.clicker(self.button3))
        self.button4.clicked.connect(lambda:self.clicker(self.button4))
        self.button5.clicked.connect(lambda:self.clicker(self.button5))
        self.button6.clicked.connect(lambda:self.clicker(self.button6))
        self.button7.clicked.connect(lambda:self.clicker(self.button7))
        self.button8.clicked.connect(lambda:self.clicker(self.button8))
        self.button9.clicked.connect(lambda:self.clicker(self.button9))
        self.button10.clicked.connect(self.reset)


        # show the app
        self.show()

    def checkWin(self):
        # across 1,4,7
        if self.button1.text() != "" and self.button1.text() == self.button4.text() and self.button1.text() == self.button7.text():
            self.win(self.button1, self.button4, self.button7)
        # across 2,5,8
        if self.button2.text() != "" and self.button2.text() == self.button5.text() and self.button2.text() == self.button8.text():
            self.win(self.button2, self.button5, self.button8)
        # across 3,6,9
        if self.button3.text() != "" and self.button3.text() == self.button6.text() and self.button3.text() == self.button9.text():
            self.win(self.button3, self.button6, self.button9)

        # down 1,2,3
        if self.button1.text() != "" and self.button1.text() == self.button2.text() and self.button1.text() == self.button3.text():
            self.win(self.button1, self.button2, self.button3)
        # down 4,5,6
        if self.button4.text() != "" and self.button4.text() == self.button5.text() and self.button4.text() == self.button6.text():
            self.win(self.button4, self.button5, self.button6)
        # down 7,8,9
        if self.button7.text() != "" and self.button7.text() == self.button8.text() and self.button7.text() == self.button9.text():
            self.win(self.button7, self.button8, self.button9)

        # diagonal 1,5,9
        if self.button1.text() != "" and self.button1.text() == self.button5.text() and self.button1.text() == self.button9.text():
            self.win(self.button1, self.button5, self.button9)
        # diagonal 3,5,7
        if self.button3.text() != "" and self.button3.text() == self.button5.text() and self.button3.text() == self.button7.text():
            self.win(self.button3, self.button5, self.button7)

    def win(self, a,b,c):
        # change the button colors to red.
        a.setStyleSheet('QPushButton {color: red;}')
        b.setStyleSheet('QPushButton {color: red;}')
        c.setStyleSheet('QPushButton {color: red;}')

        # add winner label
        self.label.setText(f"{a.text()} WINS!")

        # disable the board
        self.disable()

    def disable(self):
        # create a list of all buttons
        buttonList = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]

        # reset the buttons
        for b in buttonList:
            b.setEnabled(False)



    def clicker(self, b):
        if self.counter % 2 == 0:
            mark = "X"
            self.label.setText("O's Turn")
        else:
            mark = "O"
            self.label.setText("X's Turn")

        b.setText(mark)
        b.setEnabled(False)

        self.counter += 1

        # check if won
        self.checkWin()

    def reset(self):
        # create a list of all buttons
        buttonList = [
            self.button1,
            self.button2,
            self.button3,
            self.button4,
            self.button5,
            self.button6,
            self.button7,
            self.button8,
            self.button9,
        ]

        # reset the buttons
        for b in buttonList:
            b.setText("")
            b.setEnabled(True)

            #reset button colors
            b.setStyleSheet('QPushButton {color: #797979;}')

            
        # reset the label
        self.label.setText("X Goes First")
        
        # reset the counter
        self.counter = 0

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()