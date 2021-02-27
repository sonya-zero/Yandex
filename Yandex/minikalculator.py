import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLineEdit, QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(320, 300, 250, 140)
        self.setWindowTitle("Миникалькулятор")
        
        self.btn = QPushButton("solve", self)
        self.btn.resize(40, 25)
        self.btn.move(60, 40)
        self.btn.clicked.connect(self.solve)
        
        self.number1 = QLineEdit(self)
        self.number1.resize(60, 20)
        self.number1.move(50, 30)
        self.label1 = QLabel(self)
        self.label1.setText("N1 = ")
        self.label1.move(20, 30)
        
        self.number2 = QLineEdit(self)
        self.number2.resize(60, 20)
        self.number2.move(50, 90)
        self.label2 = QLabel(self)
        self.label2.setText("N2 = ")
        self.label2.move(20, 90)
        
        texts = ["N1 + N2 = ", "N1 - N2 = ", "N1 * N2 = ", "N1 / N2 = "]
        self.labs = [QLabel(self) for _ in range(4)]
        self.LCDs = [QLCDNumber(self) for _ in range(4)]
        for i in range(4):
            
        
        
    def do(self):
        z = eval(self.left.text())
        self.z = str(z)
        self.right.setText(self.z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())