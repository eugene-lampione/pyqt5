import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # add a title
        self.setWindowTitle("Hello World!")

        # set vertical layout
        #self.setLayout(qtw.QVBoxLayout())
        formLayout = qtw.QFormLayout()
        self.setLayout(formLayout)

        # Add stuff/widgets
        formLabel = qtw.QLabel("This is a cool label row")
        formLabel.setFont(qtg.QFont("Helvetica",24))
        
        fName = qtw.QLineEdit(self)
        lName = qtw.QLineEdit(self)

        # Add rows to app
        formLayout.addRow(formLabel)
        formLayout.addRow("First Name: ", fName)
        formLayout.addRow("Last Name: ", lName)
        formLayout.addRow(qtw.QPushButton("Press Me!", clicked= lambda: pressIt()))

        # show the app
        self.show()

        def pressIt():
            # add name to label
            formLabel.setText(f'You clicked the button, {fName.text()}!')



app = qtw.QApplication([])
mw = MainWindow()

# run the app
app.exec_()