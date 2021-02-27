import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QCheckBox,  QPlainTextEdit

class MacOrder(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.dishes = ["Гамбургер", "Чизбургер", "Картошка фри", "Кофе", "Кока-кола"]
        self.setGeometry(300, 300, 230, 280)
        self.setWindowTitle("Mac-2")
        self.recept = QPlainTextEdit('', self)
        self.recept.setDisabled(True)
        self.recept.resize(150, 120)
        self.recept.move(10, 135)
        self.menu_items = [QCheckBox(i, self) for i in self.dishes]
        for i in range(len(self.dishes)):
            self.menu_items[i].move(10, i * 20)
        self.btn = QPushButton("Order", self)
        self.btn.move(10, 105)
        self.btn.clicked.connect(self.order)
        self.out = list()


    def order(self):
        self.out.clear()
        for i in self.menu_items:
            if i.isChecked():
                self.out.append(i.text() + '\n')
        print("".join(self.out))
        out2 = f"""Ваш заказ:
{''.join(self.out)}"""
        print(out2)
        self.recept.setPlainText(out2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MacOrder()
    ex.show()
    sys.exit(app.exec())