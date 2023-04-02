# imports
from flask import Flask, redirect, request
from markupsafe import escape
from controllers import url_controller
from utils import post_utils
import db

# initialize app
app = Flask(__name__)

db_col = db.connect_to_db()

# routes
@app.route('/')
def hello_world():
    print(db_col.find_one())
    return '<h1>Hello, world!</h1>'

@app.route('/<url_key>')
def testing(url_key):
    return redirect('https://www.google.com/')

# api routes
@app.route('/api/url', methods=['POST'])
def new_url():
    if request.method == 'POST':
        body = request.get_json()
        
        # if valid payload and valid url -- success
        if post_utils.is_valid_post_payload(body):
            return url_controller.post_url(body, db_col), 200

        # 400 error, bad request
        return {
            "error": "Invalid request; please check request body."
        }, 400
    else:
        return {
            "error": f"Invalid request method. Available methods for this url: 'POST'"
        }, 400