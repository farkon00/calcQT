import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    BUTTONS_TEXTS = [
        ["MC", "MR", "MS", "M+", "M-"],
        ["⬅", "CE", "C",  "±",  "√"],
        ["7",  "8",  "9",  "/",  "%"],
        ["4",  "5",  "6",  "*",  "1/x"],
        ["1",  "2",  "3",  "-",  "="],
        ["0",  "",   ".",  "+",  ""],
    ]

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Calculator")

        self.container = QWidget() 
        self.main = QVBoxLayout()
        self.buttons = QGridLayout()

        for i in range(6):
            for j in range(5):
                if (i, j) in ((5, 1), (5, 4)): # Cells where second half of two-cell buttons lies and empty cells
                    continue
                elif (i, j) == (5, 0): # 0
                    self.buttons.addWidget(QPushButton(MainWindow.BUTTONS_TEXTS[i][j]), i, j, 1, 2)
                else:
                    self.buttons.addWidget(QPushButton(MainWindow.BUTTONS_TEXTS[i][j]), i, j)

        self.inp = QLineEdit()
        self.inp.setMinimumHeight(50)

        self.main.addWidget(self.inp)
        self.main.addLayout(self.buttons)

        self.container.setLayout(self.main)

        self.setCentralWidget(self.container)

def main():
    app = QApplication(sys.argv)

    win = MainWindow()
    win.show()

    app.exec()

if __name__ == '__main__':
    main()