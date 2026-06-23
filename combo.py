import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # add a title
        self.setWindowTitle("Hello World!")

        # set vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # create a label
        myLabel = qtw.QLabel("Pick something from the list below")
        
        # change the font size
        myLabel.setFont(qtg.QFont("Helvetica",24))

        self.layout().addWidget(myLabel)

        # create combo box
        myCombo = qtw.QComboBox(self, editable=True,insertPolicy=qtw.QComboBox.InsertAtBottom)
        # add item to combo box
        myCombo.addItem("Pepperoni", "Something")
        myCombo.addItem("Cheese", 2)
        myCombo.addItem("Mushroom", qtw.QWidget)
        myCombo.addItem("Peppers")
        myCombo.addItems(["One","Two","Three"])
        myCombo.insertItem(2,"Third Thing")
        # put combo box on the screen
        self.layout().addWidget(myCombo)

        # create a button
        myButton = qtw.QPushButton("Press Me!",clicked = lambda: pressIt())
        self.layout().addWidget(myButton)

        # show the app
        self.show()

        def pressIt():
            # add name to label
            myLabel.setText(f'You picked: {myCombo.currentText()}')


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()