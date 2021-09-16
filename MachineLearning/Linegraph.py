import matplotlib.pyplot as plt
import numpy as np
csv=open("Linegraph.csv", "r")

header_line=csv.readline().split(",")
for i,header_text in enumerate(header_line):
    header_line[i]=header_text.replace("\n","")

xlabel=header_line[0]
ylabel=header_text[1:]

xvalues=[]
yvalues=[]

for line in csv:
    data_values=line.split(",")
    for i,data_value in enumerate(data_values):
        data_values[i]=data_value.replace("\n","")
    x=data_values[0]
    y=data_values[1]
    xvalues.append(int(x))
    yvalues.append(int(y))

plt.plot(xvalues,yvalues)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()



'''x=[]
y=[]

for n in range(10,0,-1):
    y1=n**2
    y.append(y1)
    x.append(n)
plt.plot(x,y,"y-.s") # can also use dashed and dashdot. default is called solid'''