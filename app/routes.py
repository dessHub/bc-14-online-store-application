from flask import render_template, redirect, url_for
from app import app
#from models.forms import UserForm
#from collection.documents import Book


@app.route('/')   #Route to return landing page(index page)
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('sign_up.html')

@app.route('/create')
def create():
    return render_template('user.html')

@app.route('/store')
def store():
    return render_template('store.html')
