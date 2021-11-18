import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
from sklearn import linear_model

df=pd.read_csv("RegressionWithCSV.csv")
x=df[["Volume","Weight"]]
y=df["CO2"]

linemodel=linear_model.LinearRegression()
linemodel.fit(x,y)
predictedCo2=linemodel.predict([[200,150]])
print(predictedCo2)

'''x=[80,43,36,36,95,10,66,34,37,20,26,29,48,64,6,5,36,66,72,42]
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