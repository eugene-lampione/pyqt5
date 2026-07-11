from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
from PIL import Image, ImageDraw, ImageFont

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("texttoimage.ui",self)
        self.setWindowTitle("Add Text to Image!")

        # define our widgets
        self.label = self.findChild(QLabel,"label")
        self.edit = self.findChild(QLineEdit,"lineEdit")
        self.button = self.findChild(QPushButton,"pushButton")

        # click the button
        self.button.clicked.connect(self.addText)


        # show the app
        self.show()

    def addText(self):
        # grab the text
        myText = self.edit.text()

        # grab the image
        myImage = Image.open("images/eugene.jpg")

        # define the font
        myFont = ImageFont.truetype("Arial Unicode.ttf", 46)

        # edit the image
        editImage = ImageDraw.Draw(myImage)
        editImage.text((128,320), myText, ("white"), font=myFont)

        # save the image
        myImage.save("images/eugene2.jpg")

        # update app image
        pixmap = QPixmap("images/eugene2.jpg")
        self.label.setPixmap(pixmap)

        # clear the textbox
        self.edit.setText("")

        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()