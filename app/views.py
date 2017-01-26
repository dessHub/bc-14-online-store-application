from app import app, lm
from pymongo import MongoClient
from flask import request, redirect, render_template, url_for, flash
from flask.ext.login import current_user, login_user, logout_user, login_required
from .forms import LoginForm, StoreForm, ProductForm
from .user import User

@app.route('/')       #it displays index page
def home():
    stores = app.config['STORE_COLLECTION'].find({}) #retrieves registered stores from the database
    return render_template('home.html',stores=stores) #returns the index template with the stores retrieved from database

@app.route('/store/new', methods=['GET', 'POST'])   #routes to create new store
@login_required
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        store = {"title":form.title.data,"description":form.description.data,"user_id":current_user.get_id()}
        app.config['STORE_COLLECTION'].insert(store)
        return redirect(url_for('home'))
    return render_template('store_form.html', form=form)

@app.route('/product/new', methods=['GET', 'POST'])  #routes to create new product
@login_required
def new_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = {"title":form.product_name.data,"description":form.description.data,"user_id":current_user.get_id()}
        app.config['PRODUCT_COLLECTION'].insert(product)
        return redirect(url_for('new_product'))
    return render_template('product_form.html', form=form)

@app.route('/view/pstore')    #routes to render user store page
@login_required
def view_pstore():
    user = current_user.get_id()
    store = app.config['STORE_COLLECTION'].find_one({"user_id":user})
    products = app.config['PRODUCT_COLLECTION'].find({"user_id":user})
    print products
    return render_template('pstore.html', store=store, products=products)

@app.route('/view/store/<user_id>')     #routes to view individual store
def view_store(user_id):
    products = app.config['PRODUCT_COLLECTION'].find({"user_id":user_id})
    store = app.config['STORE_COLLECTION'].find_one({"user_id":user_id})
    return render_template('store.html',store=store,products=products)
