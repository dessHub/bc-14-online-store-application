from flask import render_template, redirect, url_for
from app import app
from forms import StoreForm
from document import Store

@app.route('/')                   #Route to return landing page(index page)
def index(page=1):
    title = u'Stores list'
    stores = Store.query.paginate(page=page, per_page=5)

    return render_template('index.html', stores=stores, title=title)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('sign_up.html')

@app.route('/store_form')
def store_form():
    return render_template('store_form.html', form=form)

@app.route('/store')
def store():
    return render_template('store.html')

@app.route('/api/new', methods=['GET', 'POST'])
def new_store():
    form = StoreForm()
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('new_store'))
    return render_template('store_form.html', form=form)
