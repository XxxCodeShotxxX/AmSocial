from os import urandom,environ

class Config:
    DEBUG = False
    PORT = environ.get('PORT') or 5005
    SECRET_KEY = urandom(32)
    ENV = environ.get('ENV')
    SQLALCHEMY_DATABASE_URI = "mysql://amine:test@localhost/mydatabase"

class Dev(Config):
    DEBUG = True


class Prod(Config):
    PORT = environ.get('PORT') or 8080