from flask import Flask, render_template
from database import Database
from routes.api import api
app = Flask(__name__)


@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_entry')
def add():
    return render_template('add_entry.html')

if __name__ == '__main__':
    app.run(debug=True)s