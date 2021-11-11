import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

x=[1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y=[100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

'''slope,intercept,r,p,std_err=stats.linregress(x,y)

def slopefinder(x):
    return slope*x+intercept

model=list(map(slopefinder,x))'''

polynomialmodel=np.poly1d(np.polyfit(x,y,3))

#line=np.linspace(min(x),max(x),max(y))

print(r2_score(y,polynomialmodel(x)))

plt.scatter(x,y)
#plt.plot(line,polynomialmodel(line))
plt.show()


