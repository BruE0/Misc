# only import scipy specific functions, never use "import scipy"
# PROPER USE: "from scipy import XXXXXX"

#import numpy as np
#from scipy import special
#import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as Funimation

A = np.array([0, np.sqrt(2)])
B = np.array([1, -1])
C = np.array([-1, -1])

moves = 100000
position = np.zeros([moves, 2])


position[0,:] = A

a = np.random.randint(3, size = moves)

prop = 0.5 # Proportion

for i in range(1,moves):

    if a[i] == 0:
        position[i] = (A * (1-prop) + position[i-1] * prop)
    elif a[i] == 1:
        position[i] = (B * (1-prop) + position[i-1] * prop)
    else:
        position[i] = (C * (1-prop) + position[i-1] * prop)

# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'r.', animated=True)


# def init():
#     ax.set_xlim(-2, 2)
#     ax.set_ylim(-2, 2)
#     return ln,


# def update(frame):
#     xdata = position[0:frame,1]
#     ydata = position[0:frame,0]

#     ln.set_data(xdata, ydata)
#     return ln,


#ani = Funimation(fig, update, frames=np.arange(0,moves,1),
#                     init_func=init, blit=True, interval=10)


plt.plot(position[:, 0], position[:, 1], '.')
plt.plot([ A[0], B[0], C[0] ], [ A[1], B[1], C[1] ],'r.')
plt.axis([-1.1, 1.1, -1.1, 1.5])

plt.show()