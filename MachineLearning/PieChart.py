import matplotlib.pyplot as plt

slice_names = ["Python","Java","C#","C"]#names each slice
slice_sizes = [15,90,20,14]#Sizes the slices (can be more than 100)
color_swatches = plt.pie(slice_sizes, labels = slice_names, autopct = "%1.1f%%",explode = [0.01,0.0,0.0,0.0],shadow = True, colors = ["red", "blue", "green", "magenta"])[0] #makes piechart
plt.legend(color_swatches, slice_names, loc="best")
plt.show()