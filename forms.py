from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, EqualTo, Email, Length
from wtforms import StringField, PasswordField, EmailField


class RegistrationForm(FlaskForm):
    firstname = StringField('Name', validators=[DataRequired()])
    lastname = StringField('Surname', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    password_confirmation = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])