from flask import Flask
from flask import render_template

app = Flask(__name__)

html = """<p>I will give you <br> HTML tag <br>
            So it will be <br> Inside the text </p>"""
poem = ['The people upstairs all practise ballet', 'Their living room is a bowling alley',
        'Their bedroom is full of conducted tours.', 'Their radio is louder than yours.', ]


# poem = ['a', 'b', "c"]


@app.route('/')
@app.route('/<name>/')
def hello(name='Unknown User'):
    return f'Hi, {name.capitalize()}! '


@app.route('/file/<path:file>/')
def set_path(file):
    print(type(file))
    return f'Path to file "{file}"'


@app.route('/number/<float:num>/')
def set_number(num):
    print(type(num))
    return f'Number {num}'


@app.route('/text/')
def text():
    return html


@app.route('/poems/')
def poems():
    txt = '<h1> Poem </h1>\n<p>' + '<br/>'.join(poem) + '</p>'
    print(txt)
    return txt


@app.route('/index/')
def html_index():
    context = {"title": "Personal blog", 'name': "Egor"}
    return render_template('index.html', **context)


@app.route('/if/')
def show_if():
    context = {"title": "Personal blog", 'name': "Egor", 'number': 1, 'user': 'Egor'}
    return render_template('index.html', **context)


@app.route('/cycle/')
def loop():
    context = {'title': "Loop", "poem": poem, 'number': 4}
    return render_template('index.html', **context)


@app.route('/users/')
def users():
    _users = [{'name': "Egor", 'mail': 'a@mail.com', 'phone': '+44754'},
              {'name': "Igor", 'mail': 'fsa@gmail.com', 'phone': '+4473354'}, ]
    context = {"users": _users, 'title': "Dot"}
    return render_template('index2.html', **context)


@app.route('/base/')
def base():
    context = {"title": 'Main'}
    return render_template('base.html', **context)


@app.route('/extend/')
def extend():
    context = {"title": 'New page'}
    return render_template('extend.html', **context)


if __name__ == "__main__":
    app.run()
