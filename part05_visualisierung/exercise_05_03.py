import matplotlib.pylab as plt
import numpy as np

# data 
x = np.linspace(-4*np.pi, 4*np.pi, 100)
y = np.sin(x)
my_color = []
for y_i in y:
    if y_i <= 0:
        my_color.append('b')
    else:
        my_color.append('r')
x_diamond = np.arange(-4*np.pi, 5*np.pi, np.pi)
y_diamond = np.zeros(np.shape(x_diamond))

# plot
fig, ax = plt.subplots()
ax.scatter(x,y, c=my_color)
ax.scatter(x_diamond, y_diamond, marker='D', c='k')

plt.show()