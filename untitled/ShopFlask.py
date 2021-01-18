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
        Products=list(mongo.db.FoodCollection.find())
        return render_template('BuyProducts.html', products=Products, listlength=len(Products))
    else:
        MyCart=request.form.to_dict()
        cartItems=[]
        Total=0
        for cart in MyCart:
            things=mongo.db.FoodCollection.find_one({'_id':ObjectId(cart)})
            things['_id']='this is not an obeject id'
            things['Quantity']=MyCart[cart]
            if int(things['Quantity'])>=1:
                cartItems.append(things)
            Total=int(things['Price'])*int(things['Quantity'])+Total
        session['userCart']=cartItems
        return render_template('/Checkout.html',total=Total)

@app.route('/EmptyCart')
def Empty():
    session.clear()
    return redirect('/')

@app.route('/DeleteProducts')
def delete():
    AllProducts=mongo.db.FoodCollection.find()
    return render_template('DeleteAProduct.html',allProducts=AllProducts)

@app.route("/RealDelete/<id>")
def Realdelete(id):
    deleteable=mongo.db.FoodCollection.find_one({'_id':ObjectId(id)})
    mongo.db.FoodCollection.delete_one(deleteable)
    return redirect('/DeleteProducts')

if __name__ == '__main__':
    app.run(debug=True)

#HW=do grand total and work on next project