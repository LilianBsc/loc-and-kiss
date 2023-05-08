from init import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    # Define the relationship to the other tables
    score = db.relationship('Score', backref='user', lazy=True, uselist=False)
    locs = db.relationship('Loc', backref='user', lazy=True)

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.email}"

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    
class Loc(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lattitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
