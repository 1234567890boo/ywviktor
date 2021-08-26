import matplotlib.pyplot as plt
file=open("BarGraphPlots.csv", "r")
import numpy as np

for i in file:
    list=i.split(",")

listlen=int(len(list)/2)

xlen=list[0:listlen]#xlen is names
ylen=list[listlen:]#ylen is nums
ylen2=[]#for the ints so the graph works

for u in ylen:
    ylen2.append(int(u))


bar_indexes = np.arange(len(xlen))
bar_heights = np.array(ylen2)
plt.bar(bar_indexes,bar_heights)
plt.yticks(bar_heights,ylen2)
plt.xticks(bar_indexes,xlen)
plt.show()


'''pie_slices=[50,90,20,14]
pie_names=['Python','Java','C#','C']
explode1=[0.2,0,0,0]
plt.pie(pie_slices,labels=pie_names, autopct="%1.1f%%",explode=explode1,shadow=True)
'''