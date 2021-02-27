import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 280, 70)
        
        st = ["0", "+", "-", "*"]
        
        self.setWindowTitle("Arifmometr")
        
        self.num1 = QLineEdit(self)
        self.num1.move(10, 10)
        self.num1.resize(50, 30)
        
        self.btn1 = QPushButton("+", self)
        self.btn1.move(60, 10)
        self.btn1.resize(30, 30)
        self.btn1.clicked.connect(self.solve(1))

        self.btn2 = QPushButton("-", self)
        self.btn2.move(90, 10)
        self.btn2.resize(30, 30)
        self.btn2.clicked.connect(self.solve(2))

        self.btn3 = QPushButton("*", self)
        self.btn3.move(120, 10)
        self.btn3.resize(30, 30)
        self.btn3.clicked.connect(self.solve(3))

        self.num2 = QLineEdit(self)
        self.num2.move(150, 10)
        self.num2.resize(50, 30)

        self.sign = QLabel(self)
        self.sign.move(200, 15)
        self.sign.setText(" = ")

        self.answ = QLineEdit(self)
        self.answ.setDisabled(True)
        self.answ.resize(50, 30)
        self.answ.move(215, 10)

    def solve(x, self):
        otvet = str(str(self.number1.text()) + st[x] + str(self.number2.text()))
        self.answ.setText(str(eval(otvet)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())