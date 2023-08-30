from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/contact-us/')
def contact():
    return '<h1>Call here</h1><br><p>Phone number: +44</p>'


@app.route('/about-us/')
def about():
    return '<h1>About</h1><br><p>This is a site</p>'


@app.route('/<int:num_1>/<int:num_2>/')
def sum(num_1, num_2):
    return f'{num_1} + {num_2} = {num_1 + num_2}'


@app.route("/len/<string:line>/")
def length(line):
    return f'Length of {line} is {len(line)}'


@app.route('/html/')
def html():
    return render_template("index_base.html")


@app.route('/students/')
def table():
    students = [{'name': "Egor", 'surname': "Ivanov", 'age': 22, "grade": 4.5},
                {'name': "Igor", 'surname': "Ivanov", 'age': 22, "grade": 4.5}, ]
    context = {"students": students, 'title': "Table"}
    return render_template('index_tabel.html', **context)


@app.route('/news/')
def news():
    _news = [{'news_title': "Victory", 'text': "Today we won the match", 'date': "22-02-2023"},
             {'news_title': "Flood", 'text': "Our local street got flooded", 'date': "23-02-2023"}, ]
    context = {"news": _news, 'title': "News"}
    return render_template('index_news.html', **context)


@app.route('/main/')
def main_page():
    return render_template('base.html')


@app.route('/about/')
def about_page():
    return render_template('about.html')


@app.route('/contact/')
def contact_page():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()
