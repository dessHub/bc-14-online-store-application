import datetime
from app import db
from flask.ext.mongoalchemy import BaseQuery
from wtforms import Form, BooleanField, StringField, PasswordField, validators

import re

class StoreQuery(BaseQuery):

    def starting_with(self, letter):
        regex = r'^' + letter
        return self.filter({'title': re.compile(regex, re.IGNORECASE)})

class Store(db.Document):
    query_class = StoreQuery

    title = db.StringField()
    description = db.StringField()

class User(db.Document):

    username = db.StringField()
    email = db.StringField()
    password = db.StringField()
    active = db.StringField(default=True)
    timestamp = db.DateTimeField(default=datetime.datetime.now())
