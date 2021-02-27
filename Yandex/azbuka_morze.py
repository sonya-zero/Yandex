import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

CODE = dict(a='.-', b='-...', c='-.-.', d='-..', e='.', f='..-.', g='--.', h='....', i='..', j='.---', k='-.-',
            l='.-..', m='--', n='-.', o='---', p='.--.', q='--.-', r='.-.', s='...', t='-', u='..-', v='...-', w='.--',
            x='-..-', y='-.--', z='--..')

class Morze(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 300, 400, 100)
        self.setWindowTitle("Morze-2")
        self.btns = [QPushButton(i, self) for i in CODE.keys()]
        for i in range(len(CODE)):
            self.btns[i].resize(30, 20)
            self.btns[i].move(30 * (i) + 5, 5) if i <= 12 else self.btns[i].move(30 * (i - 13) +5, 25)
            self.btns[i].clicked.connect(self.paste)
        self.pole = QLineEdit(self)
        self.pole.setDisabled(True)
        self.pole.resize(390, 40)
        self.pole.move(5, 50)
        self.text = ""

    def paste(self):
        print(CODE[self.sender().text()])
        self.text += CODE[self.sender().text()]
        self.pole.setText(self.text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Morze()
    ex.show()
    sys.exit(app.exec())