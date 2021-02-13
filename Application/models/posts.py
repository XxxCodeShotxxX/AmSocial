
from . import db
from datetime import datetime

class Posts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String(600))
    timestamp = db.Column(db.DateTime(),default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),
        nullable=False)