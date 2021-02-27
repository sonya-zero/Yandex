import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLineEdit, QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.mark = "->"
        self.setGeometry(200, 300, 310, 70)
        self.setWindowTitle("Вычисление выражений")
        self.btn = QPushButton(self.mark, self)
        self.btn.resize(40, 20)
        self.btn.move(135, 30)
        self.btn.clicked.connect(self.do)
        
        self.left = QLineEdit(self)
        self.left.resize(100,20)
        self.left.move(30, 30)
        self.right = QLineEdit(self)
        self.right.resize(100, 20)
        self.right.move(180, 30)
        self.lef = self.left.text()
        self.rig = self.right.text()
        
        self.name_label = QLabel(self)
        self.name_label.setText("Выражение: ")
        self.name_label.move(30, 15)
        self.name_label = QLabel(self)
        self.name_label.setText("Результат: ")
        self.name_label.move(180, 15)
    
    def do(self):
        z = eval(self.left.text())
        self.z = str(z)
        self.right.setText(self.z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())