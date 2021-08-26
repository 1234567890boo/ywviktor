import matplotlib.pyplot as plt
import numpy as np

x=[0,1,2,3,4,5]
y2=[]

for n in x:
    y=x[n]**2
    y2.append(y)

plt.plot(x,y2)
plt.show()

#HW:do linegraph slideshow