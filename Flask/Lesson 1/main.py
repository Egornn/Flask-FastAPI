from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 42
    return 'Hello World!'


if __name__=='__main__':
    app.run(debug = True)