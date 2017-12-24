'Models for SQL database.'
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app import login

class User(UserMixin, db.Model):
    'User model.'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        'Converts password to hash string.'
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        'Checks password against hash string.'
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    'Post model.'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

@login.user_loader
def load_user(user_id):
    'Pulls in user from database with id.'
    return User.query.get(int(user_id))