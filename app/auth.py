import json
from app import app, lm, db
from werkzeug.security import generate_password_hash
from pymongo import MongoClient
from flask import request, redirect, render_template, url_for, flash
from flask.ext.login import current_user,login_user, logout_user, login_required
from .forms import LoginForm, RegistrationForm
from .user import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = app.config['USERS_COLLECTION'].find_one({"_id": form.username.data})
        print user
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj)
            flash("Logged in successfully!", category='success')
            return redirect(request.args.get("next") or url_for("write"))
        flash("Wrong username or password!", category='error')
    return render_template('login.html', title='login', form=form)

@app.route('/user/new', methods=['GET', 'POST'])
def new_user():
    title = u'Sign Up Here'
    form = RegistrationForm()
    if form.validate_on_submit():
        passw = generate_password_hash(form.password.data, method='pbkdf2:sha256')

        user ={"first_name":form.first_name.data,"last_name":form.last_name.data,"_id":form.username.data,"email":form.email.data,"password":passw,"is_active":True}
        print user
        app.config['USERS_COLLECTION'].insert(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)




@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/write', methods=['GET', 'POST'])
@login_required
def write():
    return render_template('write.html')


@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    return render_template('settings.html')


@lm.user_loader
def load_user(username):
    u = app.config['USERS_COLLECTION'].find_one({"_id": username})
    if not u:
        return None
    return User(u['_id'])
