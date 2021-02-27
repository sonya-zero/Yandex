import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Фокус со словами')
        
        self.name_input = QLineEdit(self)
        self.name_input.move(0, 0)
        
        self.btn = QPushButton("->", self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(132, 0)
        
        self.name_input = QLineEdit(self)
        self.name_input.move(170, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())