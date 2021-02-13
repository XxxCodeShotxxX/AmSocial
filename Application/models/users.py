
from . import db
from flask_login import UserMixin

class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(250),unique=True,nullable=False)
    username = db.Column(db.String(250),unique=True,nullable=False)
    password = db.Column(db.String(250),unique=True,nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)
