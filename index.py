# imports
from flask import Flask, redirect, request
from markupsafe import escape
from controllers import url_controller
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
@app.route('/api/url', methods=['GET', 'POST'])
def new_url():
    body = request.get_json()
    
    # if valid payload and valid url -- success
    if url_controller.is_valid_post_payload(body):
        return url_controller.post_url(body), 200

    # 400 error, bad request
    return '<p>Invalid request, please try again.</p>', 400