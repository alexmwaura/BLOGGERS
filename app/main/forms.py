from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class BlogForm(FlaskForm):
    title = StringField('Blog title',validators = [Required()])
    blogs = StringField('Your Blog',validators = [Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment = TextAreaField("Type your commnet for this blog", validators = [Required()])
    submit = SubmitField('Submit')    