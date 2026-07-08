from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QPushButton, QComboBox, QMessageBox
from PyQt5 import uic
import sys
import googletrans
import textblob

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        #uic.loadUi("translate.ui",self)
        uic.loadUi("translate.ui",self)
        self.setWindowTitle("Translator App!")

        # define our widgets
        self.translateButton = self.findChild(QPushButton,"pushButton")
        self.clearButton = self.findChild(QPushButton,"pushButton_2")

        self.combo1 = self.findChild(QComboBox,"comboBox")
        self.combo2 = self.findChild(QComboBox,"comboBox_2")

        self.textedit1 = self.findChild(QTextEdit,"textEdit")
        self.textedit2 = self.findChild(QTextEdit,"textEdit_2")

        # click the buttons
        self.translateButton.clicked.connect(self.translate)
        self.clearButton.clicked.connect(self.clear)

        # add languages to combo boxes
        self.languages = googletrans.LANGUAGES
        #print(self.languages)

        # convert to list
        self.languageList = list(self.languages.values())
        #print(self.languageList)

        # add items to comboboxes
        self.combo1.addItems(self.languageList)
        self.combo2.addItems(self.languageList)

        # set default 
        self.combo1.setCurrentText("english")
        self.combo2.setCurrentText("german")

        # show the app
        self.show()

    def clear(self):
        self.textedit1.setText("")
        self.textedit1.setFocus(True)
        self.textedit2.setText("")
        self.combo1.setCurrentText("english")
        self.combo2.setCurrentText("german")
        

    def translate(self):
        try:
            # get original lanaguage key
            for key,value in self.languages.items():
                if (value == self.combo1.currentText()):
                    from_language_key = key
            
            # get to language key
            for key,value in self.languages.items():
                if (value == self.combo2.currentText()):
                    to_language_key = key

            #self.textedit1.setText(from_language_key)
            #self.textedit2.setText(to_language_key)

            # turn original in text blob
            words = textblob.TextBlob(self.textedit1.toPlainText())

            # translate words
            words = words.translate(from_lang=from_language_key, to=to_language_key)
            

            # set translation text box
            self.textedit2.setText(str(words))

        except Exception as e:
            QMessageBox.about(self,"Translator",str(e))
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()