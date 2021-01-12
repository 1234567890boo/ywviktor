from flask import Flask, render_template, request, redirect, flash
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
import random

app = Flask("Jumbled Words Python")
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/Jumbledata'
app.config['SECRET_KEY']='poopy'
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
        samewordfinder=mongo.db.jumbledwords.find_one({'word':document['word']})
        if samewordfinder is None:
            mongo.db.jumbledwords.insert_one(document)
            return redirect('/')
        else:
            flash('That word already exists')
            flash('Try another word')
            return redirect('/jumbleaword')



@app.route('/unjumbleaword',methods=['GET'])
def UnJumbleAWord():
    dataThings = list(mongo.db.jumbledwords.find().sort('time', -1))
    if request.method == 'GET':
        for doc in dataThings:
            JumbledWord=list(doc['word'])
            random.shuffle(JumbledWord)
            JumbledWord=''.join(JumbledWord)
            doc['word']=JumbledWord
        return render_template('UnjumbleAWord.html',docs=dataThings)

@app.route('/score',methods=['POST'])
def score():
    score=0
    dataThings = list(mongo.db.jumbledwords.find().sort('time', -1))
    userAnswer=list(request.form.to_dict().values())
    correctAnswer=[]
    for n in range(0, len(dataThings),1):
        correctAnswer.append(dataThings[n]['word'])
    for s in range(0,len(correctAnswer),1):
        if userAnswer[s].upper()==correctAnswer[s]:
            score+=1
    return render_template('score.html',score=score)




if __name__ == '__main__':
    app.run(debug=True)

#hw=add new word only if old one doesnt exist