from flask import Flask, render_template, request, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId

app = Flask("My Digital Diary")
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/DiaryData'
app.config['SECRET_KEY']='e'
Bootstrap(app)
mongo=PyMongo(app)

@app.route('/',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('DiarySignup.html')
    else:
        Person = request.form.to_dict()
        mongo.db.SignupCollection.insert_one(Person)
        flash('You have been registered')
        return redirect('/')

@app.route('/DiaryLogin', methods=['Get', 'Post'])
def login():
    if 'userContent' in session:
        flash("You are already logged in")
        return redirect('/DiaryPage')
    if request.method == 'GET':
        return render_template('DiaryLogin.html')
    else:
        email = request.form['Email']
        password = request.form['Password']
        user = mongo.db.SignupCollection.find_one({'Email': email, 'Password': password})
        if user is None:
            userEmail = mongo.db.SignupCollection.find_one({'Email': email})
            if userEmail is None:
                flash('Your email is wrong')
            else:
                flash('Your password is wrong')
            return redirect('/DiaryLogin')
        else:
            session['userContent'] = [user['FirstName'], user['LastName'], user['Email']]
            return redirect('/DaiaryPage')

@app.route('/DiaryPage')
def page():
    if 'userContent' not in session:
        flash("You are not logged in")
        return redirect('/')
    user = session['userContent']
    return render_template('DiaryPage.html',User=user)

@app.route('/Logout')
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)