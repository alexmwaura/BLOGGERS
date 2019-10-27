from flask import render_template,request,redirect,url_for,abort
from .import main
from ..requests import get_random
from ..models import RandomQuotes,Blogs,Comments

from .forms import BlogForm,CommentForm

@main.route("/")
def index():
    '''


    View root function that returns the index page and its data`
    '''

    quote = get_random()
    blogs = Blogs.query.all()
    
    title = "Welcome to the best blogging site"

    return render_template("index.html",title = title,quote = quote, blogs=blogs)


@main.route("/blogs",methods = ["GET","POST"])
def new_blogs():
    '''
    View root function that returns blogs
    '''

    blog_forms = BlogForm()
    
    

    if blog_forms.validate_on_submit():
        

        title = blog_forms.title.data
        blogs = blog_forms.blogs.data
        new_blogs = Blogs(title = title,blogs = blogs) 

        new_blogs.save_blog()
        

        return redirect(url_for("main.index",blogs = blogs,title = title))
        
       
        
       

    return render_template('blog.html',blog_forms = blog_forms)

# @main.route("/blog/comment/<int:id>")
# def new_commnet(id):
#     comment_form = CommentForm()



