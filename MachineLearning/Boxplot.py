import matplotlib.pyplot as plt

figure=plt.figure(1,figsize=(9,6)) #makes the boxplot
axes=figure.add_subplot(111, title="Boxplot Are cool") #adds name
axes.boxplot([[1, 2, 3, 4, 5], [6,7,8,9,10],[11,12,13,14,15]])#shows the axes each list in the list is 1 box plot
axes.set_xticklabels(["Dogs","Cats","Bats"])
plt.show()