from flask import Flask, render_template, request, send_file, redirect, flash
from flask_pymongo import PyMongo

app = Flask("Game Website")
app.config['MONGO_URI'] = 'mongodb+srv://TestUser1:test@viktors-yw-database.hgfpy.mongodb.net/GameWebsite?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/', methods=["GET","POST"])
def Home_Page():
    return render_template('HomePage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method=='POST':
        user=request.form.to_dict()
        mongo.db.GameWebsiteEmails.insert_one(user)
    return render_template('contact.html')

@app.route('/Extra_websites')
def extraweb():
    return render_template('extraWebsite.html')

@app.route('/ActualGame/<_id>/<VidLink>', methods=["GET","POST"])
def ActualGame(_id,VidLink):
    return render_template('ActualGameSite.html', Id=_id, VidLink=VidLink)

@app.route('/download/<gamefile>')
def download(gamefile):
    return send_file("GameFiles/"+gamefile,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

#HW: fix .spec file