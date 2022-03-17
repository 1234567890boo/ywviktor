import tensorflow.compat.v1 as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing
import sklearn.model_selection
tf.disable_v2_behavior()

df=pd.read_csv("IRIS.csv")
df.replace("?",-9999999,inplace=True)
#sepal_length,sepal_width,petal_length,petal_width,species

x=np.array(df.drop(["species"],1))
y=np.array(df["species"])

xtrain,ytrain,xtest,ytest=sklearn.model_selection.train_test_split(x,y,test_size=0.5)

placeholder1=tf.placeholder("float",[None,4])
placeholder2=tf.placeholder("float",[4])
#Resume below here

distance=tf.reduce_sum(tf.abs(tf.add((placeholder1,tf.negative(placeholder2))),reduction_indices=1))

pred=tf.arg_min(distance,0)

init=tf.globab_variables_initializer()
with tf.Session as sess:
    sess.run(init)
    out1=sess.run(pred)
    print(out1)

'''a=tf.Variable(2)
b=tf.Variable(3)
c=(2*a)+(3*b)
init=tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    out1=sess.run(c)
    print(out1)'''