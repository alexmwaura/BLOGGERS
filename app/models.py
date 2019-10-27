from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class RandomQuotes:

    def __init__(self, author, id, quote, permalink):
        self.author = author
        self.id = id
        self.quote = quote
        self.permalink = permalink


class User(UserMixin, db.Model):
    """
    User class to define user
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(255))

    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)

    # Relationship defining
    blogs = db.relationship("Blogs", backref='user', lazy='dynamic')
    comment = db.relationship("Comments", backref='user', lazy='dynamic')

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


class Blogs(db.Model):
    '''

    Class that holds instances of all the qblogs in the different categories
    '''

    all_blogs = []

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    blogs = db.Column(db.String)
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    date_posted = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="blogs", lazy="dynamic")

    def save_blog(self):
        """
        Function to save a blog
        """

        db.session.add(self)
        db.session.commit()

    def like_blog(self):
        """
        function that adds likes/upvotes a posted blog
        """
        self.upvotes += 1
        self.save_blog()

    def dislike_blog(self):
        """
        function that dislikes/downvotes a posted blog
        """
        self.downvotes += 1
        self.save_blog()

    @classmethod
    def get_blogs(cls, id):
        """
        function which gets a particular blog when requested by date posted
        """
        blogs = Blogs.query.all()
        return blogs

       
    @classmethod
    def clear_blogs(cls):
        '''
        Function that deletes a blog
        '''
        Blogs.all_blogs(id).clear()

class Comments(db.Model):
    '''
    Comment class that creates instances of Commnets class that will be attached to a particular blog
    '''
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blogs_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

    def save_comment(self):
        '''
        Save the comments per blog
        '''
        db.session.add(self)
        db.session.commit()

        @classmethod
        def get_comments(self, id):
            comment = Comments.query.order_by(Comments.date_posted.desc()).filter_by(blogs_id=id).all()
            return comment
