from pathlib import Path, PurePath
from flask import Flask, jsonify, render_template, url_for, request, abort, redirect, flash, make_response, session
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Comment, Post
from datetime import datetime, timedelta
from flask_wtf import FlaskForm
import secrets
from form import LoginForm, RegistrationForm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/mydatabase.db'
db.init_app(app)
app.config['SECRET_KEY'] = secrets.token_hex()
csrf = CSRFProtect(app)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        pass
    return render_template('login.html', form=form)


# @app.cli.command("init-db")
@app.route('/init-db/')
def init_db():
    db.create_all()
    return ('OK')


# @app.cli.command("-john")
@app.route('/add_user/')
def add_user():
    user = User(username='john', surname="Johnson", password='12345q', email='john@example.com')
    db.session.add(user)
    db.session.commit()
    return ('John add in DB!')


@app.route("/edit-john/")
def edit_user():
    user = User.query.filter_by(username='john').first()
    user.email = 'new_email@example.com'
    db.session.commit()
    return ('Edit John mail in DB!')


@app.route("/del-john/")
def del_user():
    user = User.query.filter_by(username='john').first()
    db.session.delete(user)
    db.session.commit()
    return ('Delete John from DB!')


@app.route("/fill-db/")
def fill_tables():
    count = 5
    # Добавляем пользователей
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', surname="Johnson", password='12345q', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()
    # Добавляем статьи
    for post in range(1, count ** 2):
        author = User.query.filter_by(username=f'user{post % count + 1}').first()
        new_post = Post(title=f'Post title {post}', content=f'Post content {post}', author=author)
        db.session.add(new_post)
    db.session.commit()
    return 'Added'


@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)


@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify(
            [{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post
             in posts])
    else:
        return jsonify({'error': 'Posts not found'})


@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title,
                         'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password =   bcrypt.generate_password_hash( form.password.data).decode('utf-8')
        surname=form.surname.data
        username= form.username.data
        user = User(username=username, surname=surname, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        return (f'User {username} {surname} {email} was added successfully')

    return render_template('register.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
