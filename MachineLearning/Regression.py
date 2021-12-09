import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from mpl_toolkits import mplot3d
import random
import pandas as pd
from sklearn import linear_model

x=np.outer(np.linspace(-1,1,15),np.ones(15))
y=x.copy().T
z=np.sin(x*3-y*2)

fig=plt.figure()
tdproj=plt.axes(projection="3d")

tdproj.plot_surface(x,y,z,cmap="viridis",edgecolor="blue") #contour3D can replace the plot_surface
plt.show()

#=========================================================================================================

'''def wf(x,y):
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
x=z*np.tan(z)
y=x*np.cos(x)
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