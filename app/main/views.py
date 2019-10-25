from flask import render_template,request,redirect,url_for
from .import main
from ..requests import get_random
from ..models import RandomQuotes

@main.route("/")
def index():
    '''


    View root function that returns the index page and its data
    '''

    quote = get_random()
    title = "Welcome to the best blogging site"

    return render_template("index.html",title = title,quote = quote)

   
