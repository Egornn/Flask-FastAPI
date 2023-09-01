from pathlib import Path, PurePath
from flask import Flask, render_template, url_for, request, abort, redirect, flash, make_response, session
from markupsafe import escape


app= Flask(__name__)


@app.route('/')
def main_page():
    return render_template("main_page.html")


@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    name = request.form.get('name')
    email = request.form.get('email')
    resp = make_response(redirect(url_for('hello')))
    resp.set_cookie('username', name)
    resp.set_cookie('useremail', email)
    return resp


@app.route('/hello/')
def hello():
    username = request.cookies.get('username')
    return render_template('hello.html', username=username)


@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.delete_cookie('username')
    resp.delete_cookie('useremail')
    return resp


if __name__=='__main__':
    app.run(debug=True)