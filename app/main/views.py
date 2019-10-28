from flask import render_template,request,redirect,url_for,abort,flash
from .import main
from ..requests import get_random
from ..models import RandomQuotes,Blogs,Comments,Subscriber
from flask_login import login_required, current_user
from ..email import mail_message
from .forms import BlogForm,CommentForm,SubscriberForm
from ..import db


@main.route("/",methods = ["GET","POST"])

def index():
    '''


    View root function that returns the index page and its data`
    '''
    
    quote = get_random()
    blogs = Blogs.query.order_by(Blogs.date_posted.desc())
    
    comment = Comments.query.all()
    title = "Welcome to the best blogging site"

    form = SubscriberForm()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber = Subscriber(email = email)
        new_subscriber.save_subsciber()

        mail_message("Subscription Received","email/welcome_subscriber",new_subscriber.email,subscriber=new_subscriber)


    return render_template("index.html",title = title,quote = quote, blogs=blogs,comment = comment,subscriber_form = form)


@main.route("/blogs",methods = ["POST","GET"])
@login_required
def new_blogs():
    '''
    View root function that returns blogs
    '''

    blog_forms = BlogForm()
    
    

    if blog_forms.validate_on_submit():
        

        title = blog_forms.title.data
        blogs = blog_forms.blogs.data
        user_id = current_user._get_current_object().id
        new_blogs = Blogs(title = title,blogs = blogs,user_id = user_id) 

        new_blogs.save_blog()

        subscriber = Subscriber.query.all()
        for subscriber in subscriber:
            mail_message("New Blog has been posted","email/new_blogs",subscriber.email,blogs = blogs)
            

        

        return redirect(url_for("main.index"))


        flash("You posted a new blog")

        
       

    return render_template('blog.html',blog_forms = blog_forms)

@main.route('/like/<blogs_id>')
@login_required
def upvote(blogs_id):
    blogs = Blogs.query.get(blogs_id)
    blogs.like_blog()

    return redirect(url_for('main.index',id=blogs_id))

@main.route('/dislike/<blogs_id>')
@login_required
def downvote(blogs_id):
    blogs = Blogs.query.get(blogs_id)
    blogs.dislike_blog()

    return redirect(url_for('main.index',id=blogs_id))    
    

@main.route("/blog/comment/<blogs_id>",methods = ["GET","POST"])
@login_required
def new_comment(blogs_id):
    comment_form = CommentForm()
    blogs = Blogs.query.filter_by(id = blogs_id).first()
    
    

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comments(comment = comment,user = current_user,blogs = blogs)
        new_comment.save_comment()

        return redirect(url_for("main.index",comment = comment))

    return render_template("comment.html",comment_form = comment_form,blogs = blogs)    



