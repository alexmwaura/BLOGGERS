from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import Subscriber
from wtforms import ValidationError

class BlogForm(FlaskForm):
    title = StringField('Blog title',validators = [Required()])
    blogs = StringField('Your Blog',validators = [Required()])
    submit = SubmitField('Submit')

class SubscriberForm(FlaskForm):
    email = StringField("Email Address",validators=[Required(),Email()])
    submit = SubmitField("Subscribe")

    def validate_email(self,data_field):
        if Subscriber.query.filter_by(email =data_field.data).first():
            raise ValidationError("Account already subscribed with that email")


class CommentForm(FlaskForm):
    comment = TextAreaField("Type your commnet for this blog", validators = [Required()])
    submit = SubmitField('Submit')    