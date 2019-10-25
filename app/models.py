from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class RandomQuotes:

    def __init__(self,author,id,quote,permalink):

        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink


class User(UserMixin,db.Model):
    '''
    User class to define user 
    '''
    __tablename__='users'


    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True, index = True)
    quotes = db.relationship("Quotes",backref = 'user',lazy = 'dynamic')
    comment = db.relationship("Comments",backref = 'user',lazy = 'dynamic')


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'



class QuotesCategory(db.Model):
    '''

    '''        

        

