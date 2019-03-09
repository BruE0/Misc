def rungekutta4(ffunction,y,t,dt):
    k1 = ffunction(y,t)
    k2 = ffunction(y+dt*k1/2, t+dt/2)
    k3 = ffunction(y+dt*k2/2, t+dt/2)
    k4 = ffunction(y+dt*k3, t+dt)
    y = y + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
    return y
