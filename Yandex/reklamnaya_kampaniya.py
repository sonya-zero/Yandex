from flask import Flask

app = Flask(__name__)

s = ["Человечество вырастает из детства.", "Человечеству мала одна планета.", "Мы сделаем обитаемыми безжизненные пока планеты.",
     "И начнем с Марса!", "Присоединяйся!"]

@app.route('/')
def index():
    return "Миссия Колонизация Марса"

@app.route('/index')
def ind():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def prmt():
    return "<br>".join(s)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')