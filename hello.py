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
        myLabel = qtw.QLabel("Hello World! What's your name?")
        
        # change the font size
        myLabel.setFont(qtg.QFont("Helvetica",18))

        self.layout().addWidget(myLabel)

        # create entry box
        myEntry = qtw.QLineEdit()
        myEntry.setObjectName("nameField")
        myEntry.setText("")
        self.layout().addWidget(myEntry)

        # create a button
        myButton = qtw.QPushButton("Press Me!",clicked = lambda: pressIt())
        self.layout().addWidget(myButton)

        # show the app
        self.show()

        def pressIt():
            # add name to label
            myLabel.setText(f'Hello {myEntry.text()}')
            # clear entry box
            myEntry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()