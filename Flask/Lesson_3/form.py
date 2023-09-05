from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length
class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    surname = StringField('Surname',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=6)])
    email = EmailField('Email',validators=[DataRequired()])
class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    surname = StringField('Surname',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(), Length(min=6)])
    email = EmailField('Email',validators=[DataRequired()])
    