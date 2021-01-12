from flask import Flask, render_template, request, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId
from flask_cors import CORS


app = Flask("Shop")
app.config['MONGO_URI']='mongodb://127.0.0.1:27017/Shopdata'
app.config['SECRET_KEY']='yee yee haircut'
Bootstrap(app)
mongo=PyMongo(app)
CORS(app)

@app.route('/',methods=['GET'])
def Landingpage():
    return render_template('ShopLandingPage.html')

@app.route('/AddProducts',methods=['GET','POST'])
def AddProduct():
    if request.method=='GET':
        return render_template('AddProducts.html')
    else:
        Food=request.form.to_dict()
        mongo.db.FoodCollection.insert_one(Food)
        return redirect('/AddProducts')

@app.route('/BuyProducts',methods=['GET','POST'])
def BuyProducts():
    if request.method=='GET':
        Products=mongo.db.FoodCollection.find()
        return render_template('BuyProducts.html', products=Products)
    else:
        MyCart=request.form.to_dict()
        cartItems=[]
        for cart in MyCart:
            things=mongo.db.FoodCollection.find_one({'_id':ObjectId(cart)})
            things['_id']='this is no an obeject id'
            things['Quantity']=MyCart[cart]
            cartItems.append(things)
        session['userCart']=cartItems
        print(session)

        return render_template('/Checkout.html')

if __name__ == '__main__':
    app.run(debug=True)

#HW=do grand total and work on next project