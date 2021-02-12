from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,EqualTo,DataRequired,Length

class SignUp(FlaskForm):
    email = StringField('Email:',validators=[
        Email('Please enter a valid email'),
        DataRequired('Required'),])
    username= StringField('Username:',validators=[DataRequired('Required'),Length(min=3,message='At least 3 letters')])
    password = PasswordField('Password',validators=[DataRequired('Required'),Length(7,message='At least 7 Letters')])
    password_confirm = PasswordField("Confirm Password:",validators=[DataRequired('Required'),Length(7,message='At least 7 Letters'),EqualTo('password')])
    submit = SubmitField('Sign Up !')

class Login(FlaskForm):
    email = StringField('Email:',validators=[
        Email('Please enter a valid email'),
        DataRequired('Required'),])
    password = PasswordField("Password:",validators=[DataRequired('Required'),Length(7,message='At least 7 Letters')])
    submit = SubmitField('Login')
