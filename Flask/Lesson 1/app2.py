from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hi, Unknown User'


@app.route('/Egor/')
def egor():
    return 'Hi, Egor'


@app.route('/Ivan/')
def ivan():
    return 'Hi, Ivan'


@app.route('/John/')
@app.route('/john/')
@app.route('/Johnny/')
@app.route('/johnny/')
def john():
    return 'Hi, John'


if __name__ == '__main__':
    app.run(debug=True)
