import matplotlib.pyplot as plt
import numpy as np
csv=open("Boxplot.csv", "r")

Column_names=csv.readline().split(",")
Boxplot_name=[]

for i,Column_name in enumerate(Column_names):
    Column_names[i]=Column_name.replace("\n","")
    Boxplot_name.append([])

print(Boxplot_name)

for line in csv:
    data_values=line.split(",")
    for i,data_value in enumerate(data_values):
        Boxplot_name[i].append(int(data_value))

print(Boxplot_name)

figure=plt.figure(1,figsize=(9,6)) #makes the boxplot
axes=figure.add_subplot(111, title="CSV Boxplot") #adds name
axes.boxplot(Boxplot_name)#shows the axes each list in the list is 1 box plot
axes.set_xticklabels(Column_names)#Names Each boxplot
plt.show()