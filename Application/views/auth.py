
from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask.globals import session
from flask_login.utils import login_user
from werkzeug.security import check_password_hash,generate_password_hash
from Application.forms.users import Login,SignUp
from Application import App
from Application.models import users
from Application.models.users import db,Users
from flask_login import LoginManager,current_user,logout_user,login_required


auth = Blueprint('auth',__name__)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    title = 'Sign Up'
    form = SignUp()
    if request.method == 'GET':
        return render_template('auth/signup.html',title=title,form=form)
    
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = Users.query.filter_by(email=email).first()
    if user:
        flash('Email Already Signed Up')
        return redirect(url_for('auth.signup'))
    
    if form.validate_on_submit():
        new_user = Users(email=email,username=username,password=generate_password_hash(password,'sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash('Signed Up !! Now Login')
        return redirect(url_for('auth.login'))

    else:
        return render_template('auth/signup.html',form=form,title=title)

@auth.route('/login',methods=['GET','POST'])
def login():
    title = 'Login'
    form = Login()
    if request.method == 'GET':
        return render_template('auth/login.html',title=title,form=form)

    email = request.form.get('email')
    password = request.form.get('password')
    user = Users.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password,password):
        flash('Check your login details and try again !!')
        return redirect(url_for('auth.login'))

    login_user(user)
    session['username'] = current_user.username
    return redirect(url_for('home.home'))

@auth.route('/logout')
@login_required
def logout():
    session.pop('username',None)
    logout_user()
    return redirect(url_for('home.home'))