from flask import Flask,Blueprint,render_template

main = Blueprint('home',__name__)

@main.route('/')
def home():
    return render_template('home/index.html')