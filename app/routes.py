from flask import render_template, redirect, url_for, request, flash, jsonify
from app import db
from mongoalchemy.session import Session
from app import app,login_manager
from forms import StoreForm, RegistrationForm
from document import Store, User
session = Session.connect('store_collection')
#session.clear_collection(User)

@app.route('/')                   #Route to return landing page(index page)
def index():
    title = u'Stores list'
    stores = session.query(Store).all()

    return render_template('index.html', stores=stores, title=title)

@app.route('/store_form')
def store_form():
    return render_template('store_form.html', form=form)

@app.route('/store')
def store():
    title = u'Users list'
    users = session.query(User).all()
    #users = User.query.filter()
    userObj = session.query(User).filter(User.email == "info@mailu.com")

    print userObj
    for user in users:
        print user, user.username
    return render_template('store.html', users=users ,title=title)

@app.route('/store/new', methods=['GET', 'POST'])
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('new_store'))
    return render_template('store_form.html', form=form)
