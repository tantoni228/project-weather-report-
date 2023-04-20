from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField, BooleanField
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login_name = StringField('Login name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
