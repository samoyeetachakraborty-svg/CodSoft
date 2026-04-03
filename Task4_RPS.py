from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QLabel
from PySide6.QtGui import QIcon
import random

app = QApplication([])
window = QWidget()
window.setWindowTitle('Rock Paper Scissor Game OX :)')
window.resize(500, 600)

layout = QVBoxLayout()
window.setLayout(layout)

button_Layout = QHBoxLayout()
layout.addLayout(button_Layout)


user_score = 0
com_score = 0
rounds = 0

Score_board = QLabel(f"Score: You {user_score} - Computer {com_score} | Rounds: {rounds}")
layout.addWidget(Score_board)

def update_scoreboard():
    Score_board.setText(f"Score: You {user_score} - Computer {com_score} | Rounds: {rounds}")

def check_winner():
    if com_score == 3:
        QMessageBox.information(window, "Game Over", "Mr Computer is the Winner!!!!!")
    elif user_score == 3:
        QMessageBox.information(window, "Game Over", "Congratulations! You are the Winner!!!!!")

def Game_info():
    QMessageBox.information(
        window,
        "Game Info",
        "Welcome to Rock Paper Scissors Game!\n\n"
        "Rules:\n"
        "- Rock beats Scissors\n"
        "- Scissors beats Paper\n"
        "- Paper beats Rock\n\n"
        "Click on your choice to play against the computer."
    )

button = QPushButton("Game INFO")
button.clicked.connect(Game_info)

def Rock():
    global user_score, com_score, rounds

    com_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    if com_choice == 'Rock':
        QMessageBox.information(window, "Result", "It's a tie! You both chose Rock.")
    elif com_choice == 'Scissors':
        QMessageBox.information(window, 'Result', "You win! Rock beats Scissors.")
        user_score += 1
        rounds += 1
    else:
        QMessageBox.information(window, 'Result', "Computer wins! Paper beats Rock.")
        com_score += 1
        rounds += 1

    update_scoreboard()
    check_winner()

def Paper():
    global user_score, com_score, rounds

    com_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    if com_choice == 'Paper':
        QMessageBox.information(window, "Result", "It's a tie! You both chose Paper.")
    elif com_choice == 'Rock':
        QMessageBox.information(window, 'Result', "You win! Paper beats Rock.")
        user_score += 1
        rounds += 1
    else:
        QMessageBox.information(window, 'Result', "Computer wins! Scissors beats Paper.")
        com_score += 1
        rounds += 1

    update_scoreboard()
    check_winner()

def Scissors():
    global user_score, com_score, rounds

    com_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    if com_choice == 'Scissors':
        QMessageBox.information(window, "Result", "It's a tie! You both chose Scissors.")
    elif com_choice == 'Paper':
        QMessageBox.information(window, 'Result', "You win! Scissors beats Paper.")
        user_score += 1
        rounds += 1
    else:
        QMessageBox.information(window, 'Result', "Computer wins! Rock beats Scissors.")
        com_score += 1
        rounds += 1

    update_scoreboard()
    check_winner()

rck_but = QPushButton("Rock")
rck_but.setIcon(QIcon("rock.png"))
rck_but.setFixedSize(150, 150)

pap_but = QPushButton('Paper')
pap_but.setIcon(QIcon("page.png"))
pap_but.setFixedSize(150, 150)

sci_but = QPushButton('Scissors')
sci_but.setIcon(QIcon("scissor.png"))
sci_but.setFixedSize(150, 150)


rck_but.clicked.connect(Rock)
pap_but.clicked.connect(Paper)
sci_but.clicked.connect(Scissors)

button_Layout.addWidget(rck_but)
button_Layout.addWidget(pap_but)
button_Layout.addWidget(sci_but)
button_Layout.addWidget(button)

window.show()
app.exec()