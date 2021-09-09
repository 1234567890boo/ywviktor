import matplotlib.pyplot as plt
import numpy as np

'''x=[]
y=[]

for n in range(10,0,-1):
    y1=n**2
    y.append(y1)
    x.append(n)
plt.plot(x,y,"y-.s") # can also use dashed and dashdot. default is called solid'''

'''csv=open("Linegraph.csv","r")
header=csv.readline().split(",")

x = []
y = []

for i,header_text in enumerate(header):
    header[i]=header_text.replace("\n","")
    x_label=header[0]
    y_label=header[1]
for line in csv:
    datas=line.split(",")
    for n,data in enumerate(datas):
        datas[n]=data.replace("\n","")
        x1=datas[0]
        y1=datas[1]
    x.append(x1)
    y.append(y1)

x2=[]
y2=[]

for u in x:
    x2.append(int(u))

for u in y:
    y2.append(int(u))

x2.sort()
y2.sort()

plt.plot(x2,y2)'''

plt.show()