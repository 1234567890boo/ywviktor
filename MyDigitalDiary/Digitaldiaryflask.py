from flask import Flask, render_template, request, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from flask_moment import Moment
from datetime import datetime
from bson.objectid import ObjectId

app = Flask("My Digital Diary")
app.config['MONGO_URI']='mongodb+srv://TestUser1:emMfEhAK9LnMxrD@viktors-yw-database.hgfpy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app.config['SECRET_KEY']='e'
Bootstrap(app)
moment=Moment(app)
mongo=PyMongo(app)

@app.route('/',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('DiarySignup.html')
    else:
        Person = request.form.to_dict()
        mongo.db.SignupCollection.insert_one(Person)
        flash('You have been registered')
        return redirect('/DiaryLogin')

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
            time = datetime.utcnow()
            session['userContent'] = [user['FirstName'], user['LastName'], user['Email'],time]
            return redirect('/DiaryPage')

@app.route('/DiaryPage', methods=['GET', 'POST'])
def page():
    if 'userContent' not in session:
        flash("You are not logged in")
        return redirect('/')
    user = session['userContent']
    time = datetime.utcnow()
    if request.method=='POST':
        text=request.form['textArea']
        mongo.db.TextCollection.insert_one({'text':text, 'time':time, 'email':user[2]})
        return redirect('/DiaryPage')
    else:
        UserText=mongo.db.TextCollection.find({'email':user[2]}).sort('time',-1)
        return render_template('DiaryPage.html', text=UserText)


@app.route('/Logout')
def logout():
    session.clear()
    flash("You have been logged out")
    return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    document=mongo.db.TextCollection.find_one({'_id':ObjectId(id)})
    mongo.db.TextCollection.delete_one(document)
    return redirect('/DiaryPage')

if __name__ == '__main__':
    app.run(debug=True)

#mongodb user password for TestUser1:emMfEhAK9LnMxrD