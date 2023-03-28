# imports
from flask import Flask
import db

# initialize app
app = Flask(__name__)

db_col = db.connect_to_db()

# routes
@app.route('/')
def hello_world():
    print(db_col.find_one())
    return '<h1>Hello, world!</h1>'
