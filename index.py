# imports
from flask import Flask, redirect, request, render_template
from controllers import url_controller
from utils import post_utils
import db

# initialize app
app = Flask(__name__)

db_col = db.connect_to_db()

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<url_key>')
def redirect_to_url(url_key):
    url_doc = url_controller.get_url({ 'id': url_key }, db_col)
    if url_doc is not None:
        return redirect(url_doc['url'])
    else:
        return redirect('/')

# api routes
@app.route('/api/url', methods=['POST'])
def new_url():
    body = request.get_json()
    
    # if valid payload and valid url -- success
    if post_utils.is_valid_post_payload(body):
        return url_controller.post_url(body, db_col), 200

    # 400 error, bad request
    return {
        "error": "Invalid request; please check request body."
    }, 400
    
@app.route('/api/url/locate', methods=['POST'])
def locate_url():
    req_body = request.get_json()

    if 'id' not in req_body and 'url' not in req_body:
        return {
            "error": "Invalid request; please check request body."
        }, 400
    
    doc = url_controller.get_url(req_body, db_col)

    if doc is not None:
        return doc
    else:
        return { "error": "Resource not found." }, 404