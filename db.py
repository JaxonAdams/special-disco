import pymongo
import os

def connect_to_db():
    connection_string = os.environ.get('CONNECTION_STRING') or 'mongodb://localhost:27017/'

    myclient = pymongo.MongoClient(connection_string)
    db = myclient['tinyurl']
    return db['tinyurl_urls']