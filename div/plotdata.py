import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y = [2,3,1,4,5,4,6,5,7,8]
xdata = []
ydata = []

fig, ax = plt.subplots()


def animate(i):
	pt = np.random.randint(1,9)
	xdata.append(x[i])
	ydata.append(y[i])

	ax.clear()
	ax.plot(xdata,ydata,'*')
#	ax.set_xlim([min(x),max(x)])
#	ax.set_ylim([min(y),max(y)])

ani = FuncAnimation(fig, animate, frames=20, interval=500, repeat=False)

plt.show()
