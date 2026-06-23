from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.count = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(458, 121)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nextButton = QtWidgets.QCommandLinkButton(self.centralwidget, clicked = lambda:self.increment())
        self.nextButton.setGeometry(QtCore.QRect(10, 0, 172, 51))
        self.nextButton.setObjectName("nextButton")
        self.nextLabel = QtWidgets.QLabel(self.centralwidget)
        self.nextLabel.setGeometry(QtCore.QRect(340, 0, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.nextLabel.setFont(font)
        self.nextLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nextLabel.setObjectName("nextLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def increment(self):
        self.count += 1

        # output to the label
        self.nextLabel.setText(str(self.count))
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nextButton.setText(_translate("MainWindow", "Increase Counter"))
        self.nextLabel.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
