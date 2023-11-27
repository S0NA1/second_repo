from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QColor, QPen, QPixmap
import sys
import random
from Ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size().width(), self.size().height())
        self.pushButton.clicked.connect(self.aply_rounds)
        self.label = QLabel()
        canvas = QPixmap(700, 700)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0)
        layout.addWidget(self.label, 1, 0)

    def aply_rounds(self):
        x, y = random.randint(10, 500), random.randint(2, 700)
        now = random.randint(0, 400)
        w, h = [now, now]
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(QColor(*[random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    app.exec_()
