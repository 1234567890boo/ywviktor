import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from mpl_toolkits import mplot3d
import random
import pandas as pd
from sklearn.datasets import load_iris as li
from sklearn import linear_model
from sklearn import metrics
from sklearn.linear_model import LogisticRegression as lr
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler as sc
from sklearn.metrics import confusion_matrix as cmd
from sklearn.metrics import accuracy_score as AS
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets._samples_generator import make_blobs

red=(0,0,255)
green=(0,255,0)
blue=(255,0,0)

import cv2
from google.colab.patches import cv2_imshow
img=cv2.imread("rgb.jpeg",cv2.IMREAD_COLOR)
line=cv2.line(img,(0,100),(75,100),green,5)
arrow=cv2.arrowedLine(img,(0,50),(75,50),green,5,tipLength=0.1) #tipLenght can be 0-1
ellipe=cv2.ellipse(img,(150,150),(25,5),30,360,0,red,2)
circle=cv2.circle(img,(150,100),25,red,2)
rect=cv2.rectangle(img,(150,10),(100,50),red,2)
text=cv2.putText(img,'CV',(250,50),cv2.FONT_HERSHEY_SIMPLEX,1,blue,3)
r,g,b=cv2.split(img)
cv2_imshow(b)
#cv2.imwrite("newimg.jpeg",g)
#use r,g,b for img for single color/grayscale or full img
cv2.waitKey(0)
cv2.destroyAllWindows()

#=========================================================================================================

'''x,y=make_blobs(n_samples=500,centers=5,random_state=0,cluster_std=0.40)

plt.scatter(x[:,0],x[:, 1],c=y,s=50,cmap='Accent')
plt.show()

#=========================================================================================================

li=li()

x=li.data
y=li.target

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=.4,random_state=1)
gnb=GaussianNB()
gnb.fit(xtrain,ytrain)

ypredict=gnb.predict(xtest)

print(metrics.accuracy_score(ytest,ypredict)*100)
print(ypredict)

#=========================================================================================================

'barwidth=0.25
subject1=[40,1,25,10,27]
subject2=[25,12,13,18,19]
subject3=[23,36,18,15,14]

bar1=np.arange(len(subject1))
bar2=[x+barwidth for x in bar1]
bar3=[x+barwidth for x in bar2]

plt.bar(bar1,subject1,color="blue",width=barwidth,label="subject1")
plt.bar(bar2,subject2,color="green",width=barwidth,label="subject2")
plt.bar(bar3,subject3,color="red",width=barwidth,label="subject3")
plt.xticks([y+barwidth for y in range(0,len(subject1),1)],['2010','2011','2012','2013','2014'])
plt.xlabel("Subjects",fontweight="bold",fontsize=17)
plt.ylabel("Percentage",fontweight="bold",fontsize=17)
plt.legend()
plt.show()

#=========================================================================================================

data=pd.read_csv('RegressionWithCSVBank.csv')

x=data.iloc[:,[2,3]].values
y=data.iloc[:,[4]].values

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20,random_state=0)

sc_x=sc()
sc_y=sc()

xtrain=sc_x.fit_transform(xtrain)
xtest=sc_x.fit_transform(xtest)

lr_xy=lr(random_state=0)
lr_xy.fit(xtrain,ytrain)

y_pred=lr_xy.predict(xtest)
cm=cmd(ytest,y_pred)
#[[true positive,false positive][true negative,false negative]]
print(AS(ytest,y_pred))


#=========================================================================================================

x=np.outer(np.linspace(-1,1,25),np.ones(25))
y=x.copy().T
z=np.sin(x*3-y*2)

fig=plt.figure()
tdproj=plt.axes(projection="3d")

#tdproj.plot_surface(x,y,z,cmap="viridis",edgecolor="blue") #Terrain
#tdproj.plot_wireframe(x,y,z,color="blue") #Wireframe
#tdproj.contour3D(x,y,z,cmap="viridis") #Contour
tdproj.scatter3D(x,y,z,color="blue") #Scatter Plot

plt.show()

#=========================================================================================================

def wf(x,y):
    return np.sin(np.sqrt(x**2++y**2))

x=np.linspace(-1,5,10)
y=np.linspace(-1,5,10)
X,Y=np.meshgrid(x,y)
Z=wf(X,Y)

fig=plt.figure()
tdproj=plt.axes(projection="3d")

tdproj.plot_wireframe(X,Y,Z,color="blue")
plt.show()

#=========================================================================================================

fig=plt.figure()
tdproj=plt.axes(projection="3d")

z=np.linspace(0,1,100)
x=z*np.sin(z) #can be sin tas or cos
y=x*np.tan(x) #can be sin tas or cos
c=x+y

tdproj.plot3D(x,y,z,"c")
plt.show()

#=========================================================================================================

np.random.seed(2)
x=np.random.normal(3,1,100)
y=np.random.normal(200,50,100)/x


train_x=x[:80]
train_y=y[:80]
test_x=x[80:]
test_y=y[80:]

line=np.linspace(0,6,100)
polynomialmodel=np.poly1d(np.polyfit(train_x,train_y,4))

r2=r2_score(test_y,polynomialmodel(test_x))
print(r2)

plt.scatter(test_x,test_y)
plt.plot(line,polynomialmodel(line))
plt.show()

#=========================================================================================================

df=pd.read_csv("RegressionWithCSV.csv")
x=df[["Volume","Weight"]]
y=df["CO2"]

linemodel=linear_model.LinearRegression()
linemodel.fit(x,y)
predictedCo2=linemodel.predict([[200,1]])
print(predictedCo2)

#=========================================================================================================

x=[80,43,36,36,95,10,66,34,37,20,26,29,48,64,6,5,36,66,72,42]
y=[20,46,3,35,67,95,51,72,58,10,26,34,90,33,38,20,56,2,47,16]

slope,intercept,r,p,std_err=stats.linregress(x,y)

def slopefinder(x):
    return slope*x+intercept

model=list(map(slopefinder,x))

line=np.linspace(min(x),max(x),max(y))

plt.scatter(x,y)
plt.plot(line,model(line))
plt.show()

polynomialmodel=np.poly1d(np.polyfit(x,y,3))

print(r2_score(y,polynomialmodel(x)))
#---------------------------------------------------------------------------------------------------------#

rand=random.randint(min(x),max(x))
polynomialmodel=np.poly1d(np.polyfit(x,y,3))
speed=polynomialmodel(rand)
print(speed,rand)

line=np.linspace(min(x),max(x),max(y))
plt.scatter(x,y)
plt.plot(line,polynomialmodel(line))
plt.show()'''