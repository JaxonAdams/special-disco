import pymongo

def connect_to_db():
    myclient = pymongo.MongoClient('mongodb://localhost:27017/')
    db = myclient['ittybitty']
    return db['ittybitty_urls']