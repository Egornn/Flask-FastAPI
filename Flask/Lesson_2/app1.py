from pathlib import Path, PurePath
from flask import Flask, render_template, url_for, request, abort, redirect, flash, make_response, session
from markupsafe import escape
from werkzeug.utils import secure_filename
import logging
import secrets

secrets.token_hex()


app= Flask(__name__)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key =b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     if request.method == 'POST':
#         # Обработка данных формы
#         flash('Form was sent!', 'success')
#         return redirect(url_for('form'))
#     return render_template('form.html')

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name']:
            flash('Type your name!', 'danger')
            return redirect(url_for('form'))
        flash('Form was sent!', 'success')
        return redirect(url_for('form'))
    return render_template('flash.html')

def get_blog(id=None):
    return None



@app.route("/path/<path:file>/")
def pathcheck(file):
        return f"Your file is here - {escape(file)}"

@app.route('/just')
def just():
     return 'hi'

# @app.route('/')
# def index():

#     context = {
#     'title': 'Main page',
#     'name': 'Egor'
#     }
#     response = make_response(render_template('main.html',
#     **context))
#     response.headers['new_head'] = 'New value'
#     response.set_cookie('username', context['name'])
#     return response

@app.route('/getcookie/')
def get_cookies():
# get cookie
    name = request.cookies.get('username')
    return f"Value of cookie: {name}"
    

@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'In num we have {num}<br>'
    text += f'Function {url_for("test_url", num=42) = }<br>'
    text += f'Function {url_for("test_url", num=42,data="new_data") = }<br>'
    text += f'Function {url_for("test_url", num=42,data="new_data", pi=3.14515) = }<br>'
    return text
        
@app.route('/about/')
def about():
    context = {'title': 'About me','name': 'Egor',}
    return render_template('about.html', **context)

@app.route('/get/')
def get():
    if level:=request.args.get('level'):
        text=f"Welcome back! Your level is {level}<br>"
    else:
     text = 'Hello, new user <br>'

    return f'{text} {request.args}'

@app.route('/submit/', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Hello {name}!'
    return render_template('form.html')

@app.get('/submit_2/')
def submit_get():
    return render_template("form.html")

@app.post('/submit_2/')
def submit_post():
    name=request.form.get(name)
    return f'Hello {name}'

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), 'uploads',file_name))
        return f"File {file_name} was uploaded"
    return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context = {
    'title': 'Page not found',
    'url': request.base_url,
    }
    return render_template('404.html', **context), 404

@app.route('/blog/<int:id>')
def get_blog_by_id(id):
    result = get_blog(id)
    if result is None:
        abort(404)
  
    

@app.route('/broken_link/')
def broken_link():
    result = broken()
    return result

@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context = {
    'title': 'Ошибка сервера',
    'url': request.base_url,
    }   
    return render_template('500.html', **context), 500

@app.route('/redirect/')
def redirect_to_index():
    return redirect(url_for('index'))


@app.route('/external')
def external_redirect():
    return redirect('https://google.com')


@app.route('/seesion/')
def index():
    if 'username' in session:
        return f'hi, {session["username"]}'
    else:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')

@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    #app.run(debug=True)
    app.run()
