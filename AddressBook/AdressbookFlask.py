from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from datetime import datetime

app = Flask("Adressbook Python")
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/data'
Bootstrap(app)
mongo=PyMongo(app)

@app.route('/',methods=['GET','POST'])
def note_saver():
    if request.method=='GET':
        dataThings=mongo.db.adressbook.find().sort('time',-1)
        return render_template('AdressbookHTML.html',name='Your Name',head='My Contacts',docs=dataThings)
    elif request.method=='POST':
        document={}
        document['note']=request.form['new-phone']
        document['time']=datetime.utcnow()
        mongo.db.Noteollection.insert_one(document)
        return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)