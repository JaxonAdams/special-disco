import pymongo

def connect_to_db():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    db = myclient['tinyurl']
    return db['tinyurl_urls']