from utils import post_utils

def post_url(req_body, db):
    # check if url already in db
    doc = db.find_one({ "url": req_body["url"] }, { "_id": 0 })

    if doc is not None:
        print(doc)
        return doc
    
    # generate id
    while True:
        new_id = post_utils.generate_id()

        if db.find_one({ "id": new_id }) is None:
            break
    
    # insert doc
    new_doc = { "id": new_id, "url": req_body["url"] }

    inserted = db.insert_one(new_doc)

    del new_doc['_id']
    return new_doc

def get_url(req_body, db):
    # return document, find by url or id
    if "id" in req_body:
        doc = db.find_one({ "id": req_body["id"] }, { "_id": 0 })
    elif "url" in req_body:
        doc = db.find_one({ "url": req_body["url"] }, { "_id": 0 })

    return doc
