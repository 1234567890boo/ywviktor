import matplotlib.pyplot as plt
import numpy as np
csv=open("PieChartCSV.csv", "r")

slice_names=csv.readline().split(",")
slice_sizes=csv.readline().split(",")
slice_explosion=[0.0,0.0,0.01,0.0]

for i, slice_name in enumerate(slice_names):
    slice_names[i]=slice_name.replace("\n","")

for i, slice_size in enumerate(slice_sizes):
    slice_sizes[i]=float(slice_size)


color_swatches = plt.pie(slice_sizes, labels = slice_names, autopct = "%1.1f%%",explode = slice_explosion,shadow = True, colors = ["red", "blue", "green", "magenta"])[0]
plt.legend(color_swatches, slice_names, loc="best")
plt.show()