import sys
import random

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.check = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.check = True
        self.update()

    def paintEvent(self, event):
        if self.check:
            painter = QPainter(self)
            painter.setPen(QPen(Qt.yellow, 1, Qt.SolidLine))
            painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
            diameter = random.randint(0, 400)
            painter.drawEllipse(40, 40, diameter, diameter)
            self.check = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
