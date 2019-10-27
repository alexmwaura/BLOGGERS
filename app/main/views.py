from flask import render_template,request,redirect,url_for,abort,flash
from .import main
from ..requests import get_random
from ..models import RandomQuotes,Blogs,Comments,Subscriber
from flask_login import login_required, current_user

from .forms import BlogForm,CommentForm

@main.route("/")

def index():
    '''


    View root function that returns the index page and its data`
    '''

    quote = get_random()
    blogs = Blogs.query.order_by(Blogs.date_posted.desc())

    comment = Comments.query.filter_by().all()
    title = "Welcome to the best blogging site"

    return render_template("index.html",title = title,quote = quote, blogs=blogs,comment = comment)


@main.route("/blogs",methods = ["GET","POST"])
@login_required
def new_blogs():
    '''
    View root function that returns blogs
    '''
    subscriber = Subscriber.query.all()
    blog_forms = BlogForm()
    
    

    if blog_forms.validate_on_submit():
        

        title = blog_forms.title.data
        blogs = blog_forms.blogs.data
        user_id = current_user._get_current_object().id
        new_blogs = Blogs(title = title,blogs = blogs,user_id = user_id) 

        new_blogs.save_blog()
        for subscriber in subscriber:
            flash("You posted a new blog")

        

        return redirect(url_for("main.index",blogs = blogs,title = title))
        
        comment = Comments.get_comments()
        
       

    return render_template('blog.html',blog_forms = blog_forms)

    

@main.route("/blog/comment",methods = ["GET","POST"])
@login_required
def new_comment():
    comment_form = CommentForm()
    blogs = Blogs.query.all()
    

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comments(comment = comment,user_id = current_user._get_current_object().id)
        new_comment.save_comment()

        return redirect(url_for("main.index",comment = comment))

    return render_template("comment.html",comment_form = comment_form)    



