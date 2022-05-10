import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Calculator")

        self.container = QWidget() 
        self.main = QVBoxLayout()
        self.buttons = QGridLayout()

        for i in range(5):
            for j in range(5):
                self.buttons.addWidget(QPushButton(), i, j)

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