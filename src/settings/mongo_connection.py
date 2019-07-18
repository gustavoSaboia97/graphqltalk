from pymongo import MongoClient

import os


database_uri = os.environ.get("DATABASE_URI")
mongo_client = MongoClient(database_uri)
database = mongo_client.person_database
