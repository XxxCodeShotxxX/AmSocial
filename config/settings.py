from os import urandom,environ

class Config:
    DEBUG = False
    PORT = environ.get('PORT') or 5005
    SECRET_KEY = urandom(32)
    ENV = environ.get('ENV')

class Dev(Config):
    DEBUG = True


class Prod(Config):
    PORT = environ.get('PORT') or 8080