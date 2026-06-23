from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

# create a DB or connect to one
conn = sqlite3.connect('mylist.db')
# create a cursor
c = conn.cursor()

# create a table
c.execute("""CREATE TABLE if not exists todo_list(list_item text) """)

# commit the changes
conn.commit()

# close the connection
conn.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.addItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.addIt())
        self.addItem_pushButton.setGeometry(QtCore.QRect(20, 50, 100, 32))
        self.addItem_pushButton.setObjectName("addItem_pushButton")
        self.clearList_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.clearIt())
        self.clearList_pushButton.setGeometry(QtCore.QRect(240, 50, 100, 32))
        self.clearList_pushButton.setObjectName("clearList_pushButton")
        self.deleteItem_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.deleteIt())
        self.deleteItem_pushButton.setGeometry(QtCore.QRect(130, 50, 100, 32))
        self.deleteItem_pushButton.setObjectName("deleteItem_pushButton")
        self.addItem_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addItem_lineEdit.setGeometry(QtCore.QRect(20, 10, 461, 30))
        self.addItem_lineEdit.setObjectName("addItem_lineEdit")
        self.myList_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.myList_listWidget.setGeometry(QtCore.QRect(20, 90, 461, 201))
        self.myList_listWidget.setObjectName("myList_listWidget")
        self.savetoDB_pushButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.saveIt())
        self.savetoDB_pushButton.setGeometry(QtCore.QRect(350, 50, 131, 32))
        self.savetoDB_pushButton.setObjectName("savetoDB_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # grab all the item from the DB
        self.grabAll()

    # grab items from the DB
    def grabAll(self):
        # create a DB or connect to one
        conn = sqlite3.connect('mylist.db')

        # create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        # commit the changes
        conn.commit()

        # close the connection
        conn.close()

        # loop through records and add to widget
        for record in records:
            self.myList_listWidget.addItem(str(record[0]))
    
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

    # save to database
    def saveIt(self):
        # create a DB or connect to one
        conn = sqlite3.connect('mylist.db')

        # create a cursor
        c = conn.cursor()

        # delete everythign in table
        c.execute("DELETE FROM todo_list;",)
        
        # create blank list to hold Todo items
        items = []

        # loop through list widget to pull out each item
        for index in range(self.myList_listWidget.count()):
            items.append(self.myList_listWidget.item(index))

        for item in items:
            #print(item.text())

            # add stuff to the table
            c.execute("INSERT INTO todo_list VALUES(:item)",
                {
                    'item':item.text(),
                }
            )

        # commit the changes
        conn.commit()

        # close the connection
        conn.close()

        # pop up box
        msg = QMessageBox()
        msg.setWindowTitle("Saved to Database!")
        msg.setText("Your To Do List is saved.")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To Do List"))
        self.addItem_pushButton.setText(_translate("MainWindow", "Add Item"))
        self.clearList_pushButton.setText(_translate("MainWindow", "Clear List"))
        self.deleteItem_pushButton.setText(_translate("MainWindow", "Delete Item"))
        self.savetoDB_pushButton.setText(_translate("MainWindow", "Save to Database"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
