from flask import Flask, render_template, request, redirect, flash
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId

app = Flask("Login System")
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/Jumbledata'
Bootstrap(app)
mongo=PyMongo(app)

@app.route('/',methods=['GET','POST'])
def signup():
    return render_template('SignupPage.html')

@app.route('/Loginpage',methods=['Get','Post'])
def login():
    return render_template('LoginPage.html')

if __name__ == '__main__':
    app.run(debug=True)