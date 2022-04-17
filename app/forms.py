# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, InputRequired
            
class MakeSubscription(FlaskForm):
    firstname = StringField("First name", validators=[DataRequired()])
    lastname = StringField("Last name", validators=[DataRequired()])
    email = EmailField("Email address", validators=[DataRequired()])
    password = PasswordField("Password", validators = [InputRequired()])


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class Search(FlaskForm):
    search = StringField("", validators=[DataRequired()])