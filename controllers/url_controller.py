from utils import post_utils

def post_url(req_body, db):
    # check if url already in db
    doc = db.find_one({ "url": req_body["url"] }, { "_id": 0 })

    if doc is not None:
        return doc
    
    # generate id
    while True:
        new_id = post_utils.generate_id()

        if db.find_one({ "id": new_id }) is None:
            break
    
    # insert doc
    new_doc = { "id": new_id, "url": req_body["url"] }

    db.insert_one(new_doc)

    return new_doc