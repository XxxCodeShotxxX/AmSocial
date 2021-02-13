
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


from flask_login import LoginManager,login_user,login_required,logout_user,current_user
import config
from os import path
from dotenv import load_dotenv
from flask import Flask,render_template

App = Flask(__name__)

APP_ROOT = os.path.join(path.dirname(__file__),"..")
DOTENV = path.join(APP_ROOT,".env")
load_dotenv(DOTENV)
App.config.from_object('config.settings.'+os.environ.get('FLASK_ENV'))

@App.errorhandler(404)
def error404(error):
    return render_template('error/404.html',error=error),404




loginmngr = LoginManager()
loginmngr.login_view = "auth.login"
loginmngr.init_app(App)

@loginmngr.user_loader
def loaduser(user_id):
    return users.Users.query.get(int(user_id))


from .views.home import main as home_bp
from .views.auth import auth as auth_bp

App.register_blueprint(home_bp)
App.register_blueprint(auth_bp)

from .models import db,users,posts

db.create_all()
db.session.commit()

migrate = Migrate(App, db)
manager = Manager(App)
manager.add_command('db', MigrateCommand)