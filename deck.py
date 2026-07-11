from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("deck.ui",self)
        self.setWindowTitle("Deal Cards!")

        # define our widgets
        self.dealerLabel = self.findChild(QLabel, 'dealerLabel')
        self.playerLabel = self.findChild(QLabel, 'playerLabel')
        self.dealerHeaderLabel = self.findChild(QLabel, 'dealerHeaderLabel')
        self.playerHeaderlabel = self.findChild(QLabel, 'playerHeaderlabel')
        self.shuffleButton = self.findChild(QPushButton,'shuffleButton')
        self.dealButton = self.findChild(QPushButton,'dealButton')

        # shuffle card
        self.shuffleCards()

        # click buttons
        self.shuffleButton.clicked.connect(self.shuffleCards)
        self.dealButton.clicked.connect(self.dealCards)

        # show the app
        self.show()

    def shuffleCards(self):
        # define our deck
        suits = ["diamonds", "hearts", "clubs", "spades"]
        values = range(2,15)
        # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace

        # Create deck
        global deck
        deck = []

        for suit in suits:
            for value in values:
                deck.append(f"{value}_of_{suit}")

        # create our players
        self.dealer = []
        self.player = []

        # grab a random card for the dealer
        card = random.choice(deck)

        # remove the card from the deck
        deck.remove(card)

        # add that card to the dealers deck
        self.dealer.append(card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{card}.png')
        self.dealerLabel.setPixmap(pixmap)

        # grab a random card for the player
        card = random.choice(deck)

        # remove the card from the deck
        deck.remove(card)

        # add that card to the players deck
        self.player.append(card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{card}.png')
        self.playerLabel.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(deck)} cards left in the deck.")

    def dealCards(self):
        try:
            # grab a random card for the dealer
            card = random.choice(deck)

            # remove the card from the deck
            deck.remove(card)

            # add that card to the dealers deck
            self.dealer.append(card)

            # output card to the screen
            pixmap = QPixmap(f'images/cards/{card}.png')
            self.dealerLabel.setPixmap(pixmap)

            # grab a random card for the player
            card = random.choice(deck)

            # remove the card from the deck
            deck.remove(card)

            # add that card to the players deck
            self.player.append(card)

            # output card to the screen
            pixmap = QPixmap(f'images/cards/{card}.png')
            self.playerLabel.setPixmap(pixmap)

            # update title bar
            self.setWindowTitle(f"{len(deck)} cards left in the deck.")

        except:

            self.setWindowTitle("Game Over!")
        

# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()