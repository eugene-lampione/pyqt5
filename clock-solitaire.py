from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QStatusBar
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime
import sys
import random
from csr import Ui_resultsBox

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # load ui file
        uic.loadUi("clock-solitaire.ui",self)
        self.setWindowTitle("Clock Solitaire!")

        self.totalSeconds = 0
        self.totalScore = 0
        self.totalCleared = 0
        self.totalTimeElapsed = 0
        self.gamesPlayed = 0
        self.gameEnded = False

        # keep track of previous card and dealt card
        self.turn = 0
        self.previousCard = ""
        self.currentCard = ""

        # define our widgets
        self.clock_1 = self.findChild(QLabel, 'clock_1')
        self.clock_2 = self.findChild(QLabel, 'clock_2')
        self.clock_3 = self.findChild(QLabel, 'clock_3')
        self.clock_4 = self.findChild(QLabel, 'clock_4')
        self.clock_5 = self.findChild(QLabel, 'clock_5')
        self.clock_6 = self.findChild(QLabel, 'clock_6')
        self.clock_7 = self.findChild(QLabel, 'clock_7')
        self.clock_8 = self.findChild(QLabel, 'clock_8')
        self.clock_9 = self.findChild(QLabel, 'clock_9')
        self.clock_10 = self.findChild(QLabel, 'clock_10')
        self.clock_11 = self.findChild(QLabel, 'clock_11')
        self.clock_12 = self.findChild(QLabel, 'clock_12')
        self.clock_13 = self.findChild(QLabel, 'clock_13')
        self.clock_13_down = self.findChild(QLabel, 'clock_13_down')
        self.gameStatus = self.findChild(QLabel, 'gameStatus')
        self.shuffleButton = self.findChild(QPushButton,'shuffleButton')
        self.dealButton_1 = self.findChild(QPushButton,'dealButton_1')
        self.dealButton_2 = self.findChild(QPushButton,'dealButton_2')
        self.dealButton_3 = self.findChild(QPushButton,'dealButton_3')
        self.dealButton_4 = self.findChild(QPushButton,'dealButton_4')
        self.dealButton_5 = self.findChild(QPushButton,'dealButton_5')
        self.dealButton_6 = self.findChild(QPushButton,'dealButton_6')
        self.dealButton_7 = self.findChild(QPushButton,'dealButton_7')
        self.dealButton_8 = self.findChild(QPushButton,'dealButton_8')
        self.dealButton_9 = self.findChild(QPushButton,'dealButton_9')
        self.dealButton_10 = self.findChild(QPushButton,'dealButton_10')
        self.dealButton_11 = self.findChild(QPushButton,'dealButton_11')
        self.dealButton_12 = self.findChild(QPushButton,'dealButton_12')
        self.dealButton_13 = self.findChild(QPushButton,'dealButton_13')
        self.statusbar = self.findChild(QStatusBar, "statusbar")

        # change status bar font
        self.statusbar.setFont(QFont('Helvetica', 14))
        self.statusbar.showMessage("Ready...Click Shuffle to Start")

        # disable clock hands card
        self.disableClockButtons()

        # hide game status label
        self.gameStatus.hide()

        # click buttons
        self.shuffleButton.clicked.connect(self.shuffleCards)
        self.dealButton_1.clicked.connect(self.dealCards_1)
        self.dealButton_2.clicked.connect(self.dealCards_2)
        self.dealButton_3.clicked.connect(self.dealCards_3)
        self.dealButton_4.clicked.connect(self.dealCards_4)
        self.dealButton_5.clicked.connect(self.dealCards_5)
        self.dealButton_6.clicked.connect(self.dealCards_6)
        self.dealButton_7.clicked.connect(self.dealCards_7)
        self.dealButton_8.clicked.connect(self.dealCards_8)
        self.dealButton_9.clicked.connect(self.dealCards_9)
        self.dealButton_10.clicked.connect(self.dealCards_10)
        self.dealButton_11.clicked.connect(self.dealCards_11)
        self.dealButton_12.clicked.connect(self.dealCards_12)
        self.dealButton_13.clicked.connect(self.dealCards_13)

        # show the app
        self.show()

    def clocker(self):
        # set seconds
        self.totalSeconds += 1
        
        # Math conversion for standard layout
        self.hours = self.totalSeconds // 3600
        self.minutes = (self.totalSeconds % 3600) // 60
        self.seconds = self.totalSeconds % 60
        
        # set number of digits
        self.statusbar.showMessage(f"Time Elapsed: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
    
    def shuffleCards(self):

        #update games ended
        self.gameEnded = False

        # remove X from King pile
        self.dealButton_13.setText("")

        # reset timer
        self.totalSeconds = 0
        self.turn = 0

        #create a timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.clocker)

        # start the time and update everysecond
        self.timer.start(1000)

        # call the clocker function
        self.clocker()

        # hide game status
        self.gameStatus.hide()

        # "deal" cards
        pixmap = QPixmap(f'images/cards/card_back_red.png')
        self.clock_1.setPixmap(pixmap)
        self.clock_2.setPixmap(pixmap)
        self.clock_3.setPixmap(pixmap)
        self.clock_4.setPixmap(pixmap)
        self.clock_5.setPixmap(pixmap)
        self.clock_6.setPixmap(pixmap)
        self.clock_7.setPixmap(pixmap)
        self.clock_8.setPixmap(pixmap)
        self.clock_9.setPixmap(pixmap)
        self.clock_10.setPixmap(pixmap)
        self.clock_11.setPixmap(pixmap)
        self.clock_12.setPixmap(pixmap)
        self.clock_13_down.setPixmap(pixmap)

        # disable able clock push buttons
        self.disableClockButtons()

        # define our deck
        suits = ["diamonds", "hearts", "clubs", "spades"]
        values = range(1,14)
        # 11 = Jack, 12 = Queen, 13 = King

        # Create deck
        self.deck = []

        for suit in suits:
            for value in values:
                self.deck.append(f"{value}_of_{suit}")


        # keep track of clock down hands
        # Create an empty container for your dynamic variables
        self.clockHandsLeft = {}

        # Dynamically generate keys and values in a loop
        for i in range(1, 14):
            variable_name = f"clock_{i}_down"
            self.clockHandsLeft[variable_name] = 4

        self.clockHandsLeft["clock_13_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # set previous and current card
        self.previousCard = self.card
        self.currentCard = self.card

        # disable clock buttons except for dealtcard
        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_13.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)

    def dealCards_1(self):
        # update turn count
        self.turn += 1

        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_1_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_1.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)

    def dealCards_2(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_2_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_2.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)

    def dealCards_3(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_3_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_3.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)

    def dealCards_4(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_4_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_4.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_5(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_5_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_5.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_6(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_6_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_6.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_7(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_7_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_7.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_8(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_8_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_8.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_9(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_9_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_9.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_10(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_10_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_10.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_11(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_11_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_11.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_12(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_12_down"] -= 1

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_12.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        
    def dealCards_13(self):
        # update turn count
        self.turn += 1
        
        # revert previous card pile
        self.revertPreviousClockPile()

        # update
        self.clockHandsLeft["clock_13_down"] -= 1
        if self.clockHandsLeft["clock_13_down"] == 0:
            pixmap = QPixmap(f'images/cards/green.png')
            self.clock_13_down.setPixmap(pixmap)
            self.dealButton_13.setText("X")
            self.dealButton_13.setStyleSheet("font: bold;font-size: 36px")

        # grab a random card
        self.card = random.choice(self.deck)
        self.dealtcard = int(self.card.split("_",1)[0])

        # updated currrent and previous cards
        self.previousCard = self.currentCard
        self.currentCard = self.card

        self.disableClockButtons(self.dealtcard)

        # remove the card from the deck
        self.deck.remove(self.card)

        # output card to the screen
        pixmap = QPixmap(f'images/cards/{self.card}.png')
        self.clock_13.setPixmap(pixmap)

        # update title bar
        self.setWindowTitle(f"{len(self.deck)} cards left in the deck.")

        self.checkGameStatus(self.dealtcard)
        

    def revertPreviousClockPile(self):
        self.previousCardNumber = int(self.previousCard.split("_",1)[0])
        
        if self.turn == 1:
            # output card to the screen
            pixmap = QPixmap(f'images/cards/green.png')
            self.clock_13.setPixmap(pixmap)
        else:
            # output card to the screen
            variable_name = f"clock_{self.previousCardNumber}_down"
            
            if self.clockHandsLeft[variable_name] == 0 or self.previousCardNumber == 13:
                pixmap = QPixmap(f'images/cards/{self.previousCard}.png')
            else:
                pixmap = QPixmap(f'images/cards/card_back_red.png')

            if self.previousCardNumber == 1:
                self.clock_1.setPixmap(pixmap)
            elif self.previousCardNumber == 2:
                self.clock_2.setPixmap(pixmap)
            elif self.previousCardNumber == 3:
                self.clock_3.setPixmap(pixmap)
            elif self.previousCardNumber == 4:
                self.clock_4.setPixmap(pixmap)
            elif self.previousCardNumber == 5:
                self.clock_5.setPixmap(pixmap)
            elif self.previousCardNumber == 6:
                self.clock_6.setPixmap(pixmap)
            elif self.previousCardNumber == 7:
                self.clock_7.setPixmap(pixmap)
            elif self.previousCardNumber == 8:
                self.clock_8.setPixmap(pixmap)
            elif self.previousCardNumber == 9:
                self.clock_9.setPixmap(pixmap)
            elif self.previousCardNumber == 10:
                self.clock_10.setPixmap(pixmap)
            elif self.previousCardNumber == 11:
                self.clock_11.setPixmap(pixmap)
            elif self.previousCardNumber == 12:
                self.clock_12.setPixmap(pixmap)
            elif self.previousCardNumber == 13:
                self.clock_13.setPixmap(pixmap)

    def checkGameStatus(self, cardnumber):
        #print(self.clockHandsLeft)

        if cardnumber == 13 and self.clockHandsLeft["clock_13_down"] == 0:
            self.gameEnded = True
            self.outcome = "GAME OVER!"
            self.outcomeColor = "red"
            self.gameStatus.show()
            self.disableClockButtons()
            pixmap = QPixmap(f'images/cards/{self.currentCard}.png')
            self.clock_13.setPixmap(pixmap)
            self.revertPreviousClockPile()
            self.timer.stop()

            # update total cleared
            self.cardsCleared = 52-len(self.deck)
            self.totalCleared += self.cardsCleared

            # updated total time elapsed
            self.totalTimeElapsed += self.totalSeconds

            # update total score
            self.gameScore = self.cardsCleared * 10
            self.totalScore += self.gameScore

        if len(self.deck) == 0:
            self.gameEnded = True
            self.outcome = "YOU WIN!"
            self.outcomeColor = "green"
            self.gameStatus.show()
            self.disableClockButtons()
            self.timer.stop()

            # update total cleared
            self.cardsCleared = 52-len(self.deck)
            self.totalCleared += self.cardsCleared

            # updated total time elapsed
            self.totalTimeElapsed += self.totalSeconds

            # update total score
            self.gameScore = self.cardsCleared * 10
            self.totalScore += self.gameScore

        if self.gameEnded:

            # show results
            self.showResults()

            # update games played
            self.gamesPlayed += 1

            # pass in results to second window.
            self.ui.gameResult.setText(self.outcome)
            self.ui.gameResult.setStyleSheet(f"color:{self.outcomeColor}")
            self.ui.cardsCleared.setText(f"Cards Cleared: {self.cardsCleared} / 52")
            self.ui.timeElapsed.setText(f"Time Elapsed: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")
            self.ui.gameScore.setText(f"Game Score: {self.gameScore}")
            self.ui.totalScore.setText(f"Total Score: {self.totalScore}")
            self.ui.totalCleared.setText(f"Total Cleared: {self.totalCleared}")
            self.ui.gamesPlayed.setText(f"Games Played: {self.gamesPlayed}")
            self.ui.averageScore.setText(f"Average Score: {self.totalScore/self.gamesPlayed}")
            self.ui.averageCleared.setText(f"Average Cleared: {self.totalCleared/self.gamesPlayed}")

    def disableClockButtons(self, cardnumber = 0):
        self.dealButton_1.setEnabled(False)
        self.dealButton_2.setEnabled(False)
        self.dealButton_3.setEnabled(False)
        self.dealButton_4.setEnabled(False)
        self.dealButton_5.setEnabled(False)
        self.dealButton_6.setEnabled(False)
        self.dealButton_7.setEnabled(False)
        self.dealButton_8.setEnabled(False)
        self.dealButton_9.setEnabled(False)
        self.dealButton_10.setEnabled(False)
        self.dealButton_11.setEnabled(False)
        self.dealButton_12.setEnabled(False)
        self.dealButton_13.setEnabled(False)

        if cardnumber == 1:
            self.dealButton_1.setEnabled(True)
        elif cardnumber == 2:
            self.dealButton_2.setEnabled(True)
        elif cardnumber == 3:
            self.dealButton_3.setEnabled(True)
        elif cardnumber == 4:
            self.dealButton_4.setEnabled(True)
        elif cardnumber == 5:
            self.dealButton_5.setEnabled(True)
        elif cardnumber == 6:
            self.dealButton_6.setEnabled(True)
        elif cardnumber == 7:
            self.dealButton_7.setEnabled(True)
        elif cardnumber == 8:
            self.dealButton_8.setEnabled(True)
        elif cardnumber == 9:
            self.dealButton_9.setEnabled(True)
        elif cardnumber == 10:
            self.dealButton_10.setEnabled(True)
        elif cardnumber == 11:
            self.dealButton_11.setEnabled(True)
        elif cardnumber == 12:
            self.dealButton_12.setEnabled(True)
        elif cardnumber == 13:
            self.dealButton_13.setEnabled(True)

    def showResults(self):
        self.results = QtWidgets.QDialog()
        self.ui = Ui_resultsBox()
        self.ui.setupUi(self.results)
        self.results.show()



# Initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()