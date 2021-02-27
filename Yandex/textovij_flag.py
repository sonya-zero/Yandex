import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('text_flag.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.color1 = radioButton.verticalLayout_2(self)
        self.color2 = radioButton.verticalLayout_3(self)
        self.color3 = radioButton.verticalLayout_4(self)

    def run(self):
        self.label.setText("цвета: ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())