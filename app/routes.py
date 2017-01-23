from app import app

@app.route('/')   #Route to return landing page(index page)
def index():
    return "Hello, World!"
