import os
import config
from os import path
from dotenv import load_dotenv
from flask import Flask,render_template
from .views.home import main


app = Flask(__name__)

APP_ROOT = os.path.join(path.dirname(__file__),"..")
DOTENV = path.join(APP_ROOT,".env")
load_dotenv(DOTENV)
app.config.from_object('config.settings.'+os.environ.get('ENV'))

@app.errorhandler(404)
def error404(error):
    return render_template('error/404.html',error=error),404


app.register_blueprint(main)