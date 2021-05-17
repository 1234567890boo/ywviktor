from flask import Flask, render_template, redirect, flash
from flask_pymongo import PyMongo

app = Flask("Game Website")
#app.config['MONGO_URI'] = ''
#mongo = PyMongo(app)

@app.route('/', methods=["GET","POST"])
def Home_Page():
    return render_template('HomePage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

#HW: work on the website