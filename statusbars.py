from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(515, 179)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.push_1())
        self.button1_pushButton.setGeometry(QtCore.QRect(10, 10, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button1_pushButton.setFont(font)
        self.button1_pushButton.setObjectName("button1_pushButton")
        self.button2_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.push_2())
        self.button2_pushButton.setGeometry(QtCore.QRect(260, 10, 241, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.button2_pushButton.setFont(font)
        self.button2_pushButton.setObjectName("button2_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 515, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # change status bar font
        self.statusbar.setFont(QFont('Helvetica', 16))
        self.statusbar.showMessage("Ready...")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Status Bar Test"))
        self.button1_pushButton.setText(_translate("MainWindow", "Button 1"))
        self.button2_pushButton.setText(_translate("MainWindow", "Clear Status Bar"))

    def push_1(self):
        self.statusbar.showMessage("I pressed button 1")

    def push_2(self):
        self.statusbar.showMessage("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
