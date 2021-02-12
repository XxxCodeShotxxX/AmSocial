
import os
import config
from os import path
from dotenv import load_dotenv
from flask import Flask,render_template

App = Flask(__name__)

APP_ROOT = os.path.join(path.dirname(__file__),"..")
DOTENV = path.join(APP_ROOT,".env")
load_dotenv(DOTENV)
App.config.from_object('config.settings.'+os.environ.get('ENV'))

@App.errorhandler(404)
def error404(error):
    return render_template('error/404.html',error=error),404

from .views.home import main as home_bp
from .views.auth import auth as auth_bp

App.register_blueprint(home_bp)
App.register_blueprint(auth_bp)

from .models import db,users

db.create_all()
db.session.commit()
