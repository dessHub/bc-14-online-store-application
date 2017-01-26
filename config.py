from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = 'no secrets'
DB_NAME = 'storedb'

DATABASE = MongoClient()[DB_NAME]
STORE_COLLECTION = DATABASE.store_collection
USERS_COLLECTION = DATABASE.users
PRODUCT_COLLECTION = DATABASE.product_collection

DEBUG = True
