from flask import Flask

app = Flask(__name__) #Creates the application object

from app import routes #imports routes modules
