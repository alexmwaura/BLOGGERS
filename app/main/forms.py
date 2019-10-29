from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from flask_wtf.file import FileField,FileAllowed
from wtforms.validators import Required,Email,EqualTo
from ..models import Subscriber,User
from wtforms import ValidationError
from flask_login import current_user

class BlogForm(FlaskForm):
    title = StringField('Blog title',validators = [Required()])
    blogs = TextAreaField('Your Blog')
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    email = StringField("Email Address",validators=[Required(),Email()])
    submit = SubmitField("Subscribe")

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email =data_field.data).first():
            raise ValidationError("Account already subscribed with that email")


class CommentForm(FlaskForm):
    comment = TextAreaField("Type your commnet for this blog")
    submit = SubmitField('Submit')    

class UpdateProfile(FlaskForm):
    username = StringField('Enter Your Username', validators=[Required()])
    email = StringField('Email Address', validators=[Required(),Email()])
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
   
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            if User.query.filter_by(email = email.data).first():
                raise ValidationError("The Email has already been taken!")
    
    def validate_username(self, username):
        if username.data != current_user.username:
            if User.query.filter_by(username = username.data).first():
                raise ValidationError("The username has already been taken")    