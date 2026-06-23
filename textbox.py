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
        myLabel = qtw.QLabel("Type something into the box below")
        
        # change the font size
        myLabel.setFont(qtg.QFont("Helvetica",24))

        self.layout().addWidget(myLabel)

        # create text box
        myText = qtw.QTextEdit(self,
            acceptRichText=False,
            html="<h1>Big Header Text</h1>",
            #plainText="this is real text",
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=50,
            placeholderText="Hello Word!",
            readOnly=False,
        )

        # put combo box on the screen
        self.layout().addWidget(myText)

        # create a button
        myButton = qtw.QPushButton("Press Me!",clicked = lambda: pressIt())
        self.layout().addWidget(myButton)

        # show the app
        self.show()

        def pressIt():
            # add name to label
            myLabel.setText(f'You typed: {myText.toPlainText()}')
            myText.setPlainText("You pressed the button")


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()