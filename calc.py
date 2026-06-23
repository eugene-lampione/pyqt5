

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # output Label
        self.outputLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputLabel.setGeometry(QtCore.QRect(10, 10, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputLabel.setObjectName("outputLabel")

        # Percent Button
        self.percentButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("%"))
        self.percentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.percentButton.setFont(font)
        self.percentButton.setObjectName("percentButton")
        
        # Clear Button
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("C"))
        self.cButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        
        # Arrow Button (clear one character)
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.removeIt())
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")

        # divide button
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("/"))
        self.divideButton.setGeometry(QtCore.QRect(275, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        
        # Nine Buttons
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        
        # Eight Buttons
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        
        # Seven Button
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        
        # Multiply Button
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(275, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        
        # Six Buttons
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        
        # Five button
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        
        # Four Button
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        
        # Minus Button
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("-"))
        self.minusButton.setGeometry(QtCore.QRect(275, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        
        # Three Button
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        
        # Two Button
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        
        # One Button
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        
        # Add Button
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("+"))
        self.addButton.setGeometry(QtCore.QRect(275, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        
        # Decimal Button
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.dotIt())
        self.decimalButton.setGeometry(QtCore.QRect(190, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        
        # Zero Button
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.pressIt("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        
        # Plus/Minus Button
        self.plusMinusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.plusMinusIt())
        self.plusMinusButton.setGeometry(QtCore.QRect(10, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusMinusButton.setFont(font)
        self.plusMinusButton.setObjectName("plusMinusButton")
        
        # Equal Button
        self.equalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.mathIt())
        self.equalButton.setGeometry(QtCore.QRect(275, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        
        # Main Window
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # remove a character
    def removeIt(self):
        # grb what is on the screen already
        screen = self.outputLabel.text()
        # remove last item in the list/string
        screen = screen[:-1]
        # output to screen
        self.outputLabel.setText(screen)
    
    # change postive/negative
    def plusMinusIt(self):
        # grb what is on the screen already
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-",""))
        else:
             self.outputLabel.setText(f'-{screen}')

    # add a decimal
    def dotIt(self):
        # grb what is on the screen already
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputLabel.setText(f'{screen}.')
    
    # Do the Math
    def mathIt(self):
        # grb what is on the screen already
        screen = self.outputLabel.text()
        try :
            # do the math
            answer = eval(screen)
            # output answer to the screen
            self.outputLabel.setText(str(answer))
        except:
            # output the error to the screen
            self.outputLabel.setText('ERROR')


    def pressIt(self, pressed):
        if pressed == "C":
            self.outputLabel.setText("0")
        else:
            # check to see if starts with 0, and delete 0
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")
            # Concatenate pressed button with what was there already
            self.outputLabel.setText(f'{self.outputLabel.text()}{pressed}')
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputLabel.setText(_translate("MainWindow", "0"))
        self.percentButton.setText(_translate("MainWindow", "%"))
        self.cButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.multiplyButton.setText(_translate("MainWindow", "X"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.decimalButton.setText(_translate("MainWindow", "."))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.plusMinusButton.setText(_translate("MainWindow", "+/-"))
        self.equalButton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
