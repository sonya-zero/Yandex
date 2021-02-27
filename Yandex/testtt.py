from flask import Flask

app = Flask(__name__)


@app.route('/')

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)

@app.route('/index')
def index():
    return "Привет, Яндекс!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')