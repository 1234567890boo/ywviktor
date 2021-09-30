import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

figure, axes = plt.subplots()

axes.set_xlim(-5, 20)
axes.set_ylim(-5, 30)

line, = plt.plot([], [], 'g-', animated=True)
line2, = plt.plot([], [], 'g-', animated=True)

x_values = []
y_values = []

x_values2=[]
y_values2=[]


def update(frame):
    y_values.append(frame)
    x_values.append(math.sin(frame))
    y_values2.append(frame)
    x_values2.append(math.cos(frame))
    line.set_data(x_values, y_values)
    line2.set_data(x_values2, y_values2)
    return line,line2,

animaton=FuncAnimation(figure,update,frames=np.arange(0,30,0.5),blit=True,repeat=False)
plt.show()