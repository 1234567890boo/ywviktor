import matplotlib.pyplot as plt
import numpy as np

x=[5,1,8,3,9]
y=[1,6,2,6,10]
plt.scatter(x,y)


pie_slices=[50,90,20,14]
pie_names=['Python','Java','C#','C']
explode1=[0.2,0,0,0]
plt.pie(pie_slices,labels=pie_names, autopct="%1.1f%%",explode=explode1,shadow=True)
plt.show()