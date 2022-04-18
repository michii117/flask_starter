# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
            
class MakeSubscription(FlaskForm):
    firstname = StringField("First name", validators=[DataRequired()])
    lastname = StringField("Last name", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators = [InputRequired()])


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])

class Search(FlaskForm):
    search = StringField("", validators=[DataRequired()])

class Prospects(FlaskForm):
    firstname = StringField("First name*", validators=[DataRequired()])
    lastname = StringField("Last name*", validators=[DataRequired()])
    email = EmailField("Email*", validators=[DataRequired()])
    number = StringField("Phone number*", validators=[DataRequired()])
    companytype = StringField("Company type*", validators=[DataRequired()])
    companyname = StringField("Company*", validators=[DataRequired()])
    jobtitle = StringField("Job title*", validators=[DataRequired()])
    adverttitle = StringField("Advert title*", validators=[DataRequired()])
    advertdescription = TextAreaField("Advert Description")
    advertphoto = FileField('Advert photo:*', validators=[FileRequired(), FileAllowed(['jpg', 'png'],'Image Files Only!')])
