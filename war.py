from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QTextEdit, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
import sys
import random

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("war.ui",self)
        self.setWindowTitle("Deal Cards!")

        # define our widgets
        self.dealerLabel = self.findChild(QLabel, 'dealerLabel')
        self.playerLabel = self.findChild(QLabel, 'playerLabel')
        self.playerLabel2 = self.findChild(QLabel, 'playerLabel_2')
        self.dealerHeaderLabel = self.findChild(QLabel, 'dealerHeaderLabel')
        self.playerHeaderlabel = self.findChild(QLabel, 'playerHeaderLabel')
        self.shuffleButton = self.findChild(QPushButton,'shuffleButton')
        self.dealButton = self.findChild(QPushButton,'dealButton')

        # shuffle card
        self.shuffleCards()

        # click buttons
        self.shuffleButton.clicked.connect(self.shuffleCards)
        self.dealButton.clicked.connect(self.dealCards)
        self.playerLabel2.connect(self.dealCards)

        # show the app
        self.show()

    def shuffleCards(self):
        # define our deck
        suits = ["diamonds", "hearts", "clubs", "spades"]
        values = range(2,15)
        # 11 = Jack, 12 = Queen, 13 = King, 14 = Ace

        # Create deck
        #global deck
        self.deck = []

        for suit in suits:
            for value in values:
                self.deck.append(f"{value}_of_{suit}")

        # create our players
        self.dealer = []
        self.player = []

        # keep track of score
        self.dealer_score = 0
        self.player_score = 0

        # grab a random card for the dealer
        self.dealer_card = random.choice(self.deck)

        # remove the card from the deck
        self.deck.remove(self.dealer_card)

        # add that card to the dealers deck
        self.dealer.append(self.dealer_card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.dealer_card}.png')
        self.dealerLabel.setPixmap(pixmap)

        # grab a random card for the player
        self.player_card = random.choice(self.deck)

        # remove the card from the deck
        self.deck.remove(self.player_card)

        # add that card to the players deck
        self.player.append(self.player_card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.player_card}.png')
        self.playerLabel.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        # determine score
        self.score()

    def dealCards(self):
        try:
            # grab a random card for the dealer
            self.dealer_card = random.choice(self.deck)

            # remove the card from the deck
            self.deck.remove(self.dealer_card)

            # add that card to the dealers deck
            self.dealer.append(self.dealer_card)

            # output card to the screen
            pixmap = QPixmap(f'images/cards/{self.dealer_card}.png')
            self.dealerLabel.setPixmap(pixmap)

            # grab a random card for the player
            self.player_card = random.choice(self.deck)

            # remove the card from the deck
            self.deck.remove(self.player_card)

            # add that card to the players deck
            self.player.append(self.player_card)

            # output card to the screen
            pixmap = QPixmap(f'images/cards/{self.player_card}.png')
            self.playerLabel.setPixmap(pixmap)

            # update title bar
            self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

            # determine score
            self.score()

        except:
            # TIE
            if self.dealer_score == self.player_score:
                self.setWindowTitle(f"Game Over! - IT'S A TIE! - {self.dealer_score} to {self.player_score}")

            # Dealer Wins
            elif self.dealer_score > self.player_score:
                self.setWindowTitle(f"Game Over! - Dealer Wins! - {self.dealer_score} to {self.player_score}")

            # player wins
            else:
                self.setWindowTitle(f"Game Over! - Player Wins! - {self.dealer_score} to {self.player_score}")


    def score(self):
        # strip out the card number
        self.dealer_card = int(self.dealer_card.split("_",1)[0])
        self.player_card = int(self.player_card.split("_",1)[0])

        # compare card numbers
        # tie
        if self.dealer_card == self.player_card:
            # update dealer/player header labels
            self.dealerHeaderLabel.setText("Tie!")
            self.playerHeaderlabel.setText("Tie!")

            # update title bar
            self.setWindowTitle(f"{len(self.deck)} cards left in the deck    ||     Dealer: {self.dealer_score} - Player: {self.player_score}")

        # dealer wins
        elif self.dealer_card > self.player_card:
            # update dealer/player header labels
            self.dealerHeaderLabel.setText("Dealer Wins!")
            self.playerHeaderlabel.setText("Player Loses")
            # update dealer score
            self.dealer_score += 1

            # update title bar
            self.setWindowTitle(f"{len(self.deck)} cards left in the deck    ||     Dealer: {self.dealer_score} - Player: {self.player_score}")

        # player wins
        else:
            # update dealer/player header labels
            self.dealerHeaderLabel.setText("Dealer Loses!")
            self.playerHeaderlabel.setText("Player Wins")
            # update player score
            self.player_score += 1

            # update title bar
            self.setWindowTitle(f"{len(self.deck)} cards left in the deck    ||     Dealer: {self.dealer_score} - Player: {self.player_score}")


# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()