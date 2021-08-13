import matplotlib.pyplot as plt
import numpy as np

bar_names = np.array(["Dogs", "Cats", "Monkeys", "Beatles", "Elephants", "Snakes"]) #makes bars with names
bar_indexes = np.arange(len(bar_names))#aranges the bars by name length
bar_heights = np.array([50, 80, 12, 19, 89, 10])#sizes the bars in the bar graph
plt.ylabel("Number of animals") #labels the y axis
plt.title("Animals")#titles the bar graph

plt.bar(bar_indexes, bar_heights, align="center") #makes graph
plt.xticks(bar_indexes, bar_names) #makes graph
plt.show()#shows the graph

#Homework: do bargraph slide 5