from Application import APP_ROOT
from os import urandom,environ,path

class Config:
    DEBUG = False
    PORT = environ.get('PORT') or 5005
    SECRET_KEY = urandom(32)
    ENV = environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI') or ('sqlite:///' + path.join(APP_ROOT, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Dev(Config):
    DEBUG = True


class Prod(Config):
    PORT = environ.get('PORT') or 8080