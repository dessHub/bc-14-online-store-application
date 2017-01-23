from flask import render_template
from app import app

@app.route('/')   #Route to return landing page(index page)
def index():
    return render_template('index.html')
