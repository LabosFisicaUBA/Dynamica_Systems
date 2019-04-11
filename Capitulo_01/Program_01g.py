# Program 01g: A program that animates a simple curve.
#http://louistiao.me/posts/notebooks/embedding-matplotlib-animations-in-jupyter-notebooks/
# Remember to run the Module (or type F5).
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from IPython.display import HTML
fig = plt.figure(1)
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
plt.xlabel('time')
plt.ylabel('sin($\omega$t)')
def init():
	line.set_data([], [])
	return line,
# The function to animate.
def animate(i):
	x = np.linspace(0, 2, 1000)
	y = np.sin(2 * np.pi * (0.1 * x * i))
	line.set_data(x, y)
	return line,

# Note: blit=True means only re-draw the parts that have changed.
anim=animation.FuncAnimation(fig, animate, init_func=init,frames=100, interval=200, blit=True)
#plt.show()
HTML(anim.to_html5_video())