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

        # create spin box
        mySpin = qtw.QDoubleSpinBox(self, 
            value=10.5,
            maximum=100,
            minimum=0,
            singleStep=20.5,
            prefix="Your Order is #",
        )
        # change font size of spin box
        mySpin.setFont(qtg.QFont("Helvetica",18))
        
        # put combo box on the screen
        self.layout().addWidget(mySpin)

        # create a button
        myButton = qtw.QPushButton("Press Me!",clicked = lambda: pressIt())
        self.layout().addWidget(myButton)

        # show the app
        self.show()

        def pressIt():
            # add name to label
            myLabel.setText(f'You picked: {mySpin.value()}')


app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()