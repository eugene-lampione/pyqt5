from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(375, 395)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.addIt())
        self.addItem_pushButton.setGeometry(QtCore.QRect(20, 50, 100, 32))
        self.addItem_pushButton.setObjectName("addItem_pushButton")
        self.clearList_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clearIt())
        self.clearList_pushButton.setGeometry(QtCore.QRect(260, 50, 100, 32))
        self.clearList_pushButton.setObjectName("clearList_pushButton")
        self.deleteItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.deleteIt())
        self.deleteItem_pushButton.setGeometry(QtCore.QRect(140, 50, 100, 32))
        self.deleteItem_pushButton.setObjectName("deleteItem_pushButton")
        self.addItem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addItem_lineEdit.setGeometry(QtCore.QRect(20, 10, 341, 30))
        self.addItem_lineEdit.setObjectName("addItem_lineEdit")
        self.myList_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.myList_listWidget.setGeometry(QtCore.QRect(20, 90, 341, 201))
        self.myList_listWidget.setObjectName("myList_listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 375, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Add Item to the list
    def addIt(self):
        # grab item from list box
        item = self.addItem_lineEdit.text()

        # add item to list
        self.myList_listWidget.addItem(item)

        # clear the item box
        self.addItem_lineEdit.setText("")

    # clear the list
    def clearIt(self):
        self.myList_listWidget.clear()

    # delete item from the list
    def deleteIt(self):
        # grab the selected/current row
        clickedRow = self.myList_listWidget.currentRow()

        # delete the selected row
        self.myList_listWidget.takeItem(clickedRow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.clearList_pushButton.setText(_translate("MainWindow", "Clear List"))
        self.deleteItem_pushButton.setText(_translate("MainWindow", "Delete Item"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
