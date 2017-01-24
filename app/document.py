
from app import db
from flask.ext.mongoalchemy import BaseQuery
import re

class StoreQuery(BaseQuery):

    def starting_with(self, letter):
        regex = r'^' + letter
        return self.filter({'title': re.compile(regex, re.IGNORECASE)})

class Store(db.Document):
    query_class = StoreQuery

    title = db.StringField()
    description = db.StringField()
    
