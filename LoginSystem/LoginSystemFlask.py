from flask import Flask, render_template, request, redirect, flash
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId

app = Flask("Login System")
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/Jumbledata'
app.config['SECRET_KEY']='dootdoot'
Bootstrap(app)
mongo=PyMongo(app)

@app.route('/',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('SignupPage.html')
    else:
        Person =request.form.to_dict()
        mongo.db.FoodCollection.insert_one(Person)
        message=flash('You have been regestered')
        return render_template('SignupPage.html', Message=message)

@app.route('/Loginpage',methods=['Get','Post'])
def login():
    if request.method == 'GET':
        return render_template('LoginPage.html')
    else:
        return redirect('LoginPage')

@app.route('/Realpage')
def page():
    return render_template('RealPage.html')

if __name__ == '__main__':
    app.run(debug=True)