import numpy as np
import matplotlib.pyplot as plt

def function(x,t): # x = array
    f = np.array([x[1], -9.8])
    return f

def rungekutta4(ffunction,y,t,dt):
    k1 = ffunction(y,t)
    k2 = ffunction(y+dt*k1/2, t+dt/2)
    k3 = ffunction(y+dt*k2/2, t+dt/2)
    k4 = ffunction(y+dt*k3, t+dt)
    y = y + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    return y

ti = 0
tf = 5
dt = 0.001

Nt = round((tf-ti) / dt)

y = np.zeros(2)
w = np.zeros((3,Nt+1))

y[0] = 10 # x0
y[1] = 0  # Vx0

w[0][0] = y[0]
w[1][0] = y[1]

for n in range(1,Nt+1):
    t = n * dt
    y = rungekutta4(function,y,t,dt)
    if ( y[0] < (1e-6) and (y[1] < 0) ):
        y[1] = -0.5 * y[1]

    w[0][n] = y[0]
    w[1][n] = y[1]
    w[2][n] = t

x = np.linspace(ti,tf,Nt+1,endpoint=True)

plt.figure(1)
plt.subplot(211)

plt.plot(x,w[0],'.')
plt.plot([0, 10],[0, 0])
plt.ylabel(r'x (m)')

plt.minorticks_on()
plt.grid(True, 'both')

plt.subplot(212)

plt.plot(x,w[1],'r.')
plt.ylabel(r'$v_{x}$ (m/s)')
plt.xlabel(r'time (s)')
plt.minorticks_on()
plt.grid(True, 'both')

plt.show()