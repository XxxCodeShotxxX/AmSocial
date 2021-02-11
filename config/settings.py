from os import urandom,environ

class Config:
    DEBUG = False
    PORT = environ.get('PORT') or 5005
    


class Dev(Config):
    pass


class Prod(Config):
    pass