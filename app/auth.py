from flask import render_template, redirect, url_for, request, flash
from app import db
from mongoalchemy.session import Session
from app import app,login_manager, flask_bcrypt
from forms import StoreForm, RegistrationForm, LoginForm
#from libs.test_user import User
from document import Store, User
from flask.ext.login import (current_user, login_required, login_user, logout_user, confirm_login, fresh_login_required)

session = Session.connect('store_collection')

@app.route('/user/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print email, password
        userObj = session.query(User).all()
        for person in userObj:
            if person.email == email and person.password == password:
                user = person


        #user = session.query(User).one().get_by_email_w_password(email)
             	if user :
        			login_user(user)
        			flash("Logged in!")
        			return redirect('/store/new')

                flash("unable to log you in")
    return render_template("login.html", form=form)

@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    title = u'Sign Up Here'
    form = RegistrationForm()
    if form.validate_on_submit():
        #password = flask_bcrypt.generate_password_hash(form.password.data)
        #user = User(form.username.data,form.email.data,password)
        form.save()
        flash('Thanks for registering')
        return redirect(url_for('index'))
    return render_template('sign_up.html', form=form)


@login_manager.unauthorized_handler
def unauthorized_callback():
	return redirect('/login')

@login_manager.user_loader
def load_user(id):
	if id is None:
		redirect('/login')
	user = User()
	user.get_by_id(id)
	if user.is_active():
		return user
	else:
		return None
