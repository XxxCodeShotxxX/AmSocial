
from . import db


class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(250),unique=True,nullable=False)
    username = db.Column(db.String(250),unique=True,nullable=False)
    password = db.Column(db.String(250),unique=True,nullable=False)
