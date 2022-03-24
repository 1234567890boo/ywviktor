import tensorflow.compat.v1 as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing
import sklearn.model_selection
tf.disable_v2_behavior()

df=pd.read_csv("cancer.csv")
df.replace("?",-9999999,inplace=True)
#sepal_length,sepal_width,petal_length,petal_width,species

testdata=[5.7,2.9,5.0,1.9]
x=np.array(df.drop(["id","diagnosis"],1))
y=np.array(df["diagnosis"])
print(x[0],len(x[0]))
print(y[0])
xtrain,xtest,ytrain,ytest=sklearn.model_selection.train_test_split(x,y,test_size=0.5)

train=tf.placeholder("float", [None, 30])
test=tf.placeholder("float", [30])

#distance=tf.reduce_sum(tf.abs(tf.add((placeholder1,tf.negative(placeholder2))),reduction_indices=1))
distance=tf.reduce_sum(tf.abs(train - test), reduction_indices=1)

pred=tf.arg_min(distance,0)

init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    out2=[]
    correctcounter=0
    for i in range(0,len(xtest),1):
        dist1=sess.run(distance, {train:xtrain, test:xtest[i]})
        out1=sess.run(pred, {train:xtrain, test:xtest[i]})
        if ytrain[out1]==ytest[i]:
            correctcounter += 1
            print("ytrain:"+ytrain[out1]+" ytest:"+ytest[i])
    print(correctcounter,len(ytest))


'''a=tf.Variable(2)
b=tf.Variable(3)
c=(2*a)+(3*b)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    out1=sess.run(c)
    print(out1)'''