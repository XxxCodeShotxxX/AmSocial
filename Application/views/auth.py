from re import I, T
from flask import Blueprint,render_template,request,flash
from Application.forms.users import Login,SignUp
auth = Blueprint('auth',__name__)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    title = 'Sign Up'
    form = SignUp()
    if request.method == 'GET':
        return render_template('auth/signup.html',title=title,form=form)
    

@auth.route('/login',methods=['GET','POST'])
def login():
    title = 'Login'
    form = Login()
    if request.method == 'GET':
        return render_template('auth/login.html',title=title,form=form)
    return render_template('auth/login.html',title=title,form=form)

@auth.route('/logout')
def logout():
    return 'logout'