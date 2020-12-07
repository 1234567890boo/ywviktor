from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId

app = Flask("Jumbled Words Python")
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/data'
Bootstrap(app)
mongo=PyMongo(app)

@app.route('/',methods=['GET'])
def Landingpage():
    return render_template('JumbledwordsLandingPage.html')

@app.route('/jumbleaword',methods=['Get','Post'])
def JumbleAWord():
    if request.method == 'GET':
        return render_template('JumbleAWord.html')
    elif request.method=='POST':
        document={}
        document['word']=request.form['word'].strip().upper()
        document['time']=datetime.utcnow()
        mongo.db.jumbledwords.insert_one(document)
        return redirect('/')


@app.route('/unjumbleaword',methods=['GET','POST'])
def UnJumbleAWord():
    if request.method == 'GET':
        dataThings = list(mongo.db.jumbledwords.find().sort('time', -1))
        return render_template('UnjumbleAWord.html',docs=dataThings)
    if request.method=='POST':
        return redirect('/score')

@app.route('/score')
def score():
    if request.method=='GET':
        return render_template('Score.html')
    elif request.method=='POST':
        return redirect('/')




if __name__ == '__main__':
    app.run(debug=True)

#hw=do the jumble a word and show in unbumble a word