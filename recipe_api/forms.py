from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class UserLoginForm(FlaskFrom):
    email = StringField('Email' validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_button = SubmitField()