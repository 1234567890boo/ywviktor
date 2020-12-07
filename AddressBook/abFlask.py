from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId

app = Flask("Adressbook Python")
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/Data'
Bootstrap(app)
mongo=PyMongo(app)

@app.route('/',methods=['GET','POST'])
def note_saver():
    if request.method=='GET':
        dataThings=list(mongo.db.adressbook.find().sort('time',-1))
        return render_template('AdressbookHTML.html',name='Your Name',head='My Contacts',docs=dataThings)
    elif request.method=='POST':
        document={}
        document['phone']=request.form['phone']
        document['name']=request.form['name']
        document['time']=datetime.utcnow()
        mongo.db.adressbook.insert_one(document)
        return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    document=mongo.db.adressbook.find_one({'_id':ObjectId(id)})
    print(document)
    mongo.db.adressbook.delete_one(document)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

#HW=use retuned id to delete item in list if done do jumbled words