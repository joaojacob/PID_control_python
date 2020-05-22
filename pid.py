import time
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand
from scipy import signal




def PID(kp, ki, kd, setPoint, sinal,previousTime = None, lastSinal = None, I= None):

    error = setPoint - sinal
    now = time.time()

    timePass = now - (previousTime if previousTime is not None else now)

    previousTime = now

    P = error * kp

    I = (I if I is not None else 0)*(error * ki) * timePass

    if timePass == 0:
        D = (lastSinal if lastSinal is not None else sinal) - sinal * (1)
    else:
        D = (lastSinal if lastSinal is not None else sinal) - sinal * (kd/timePass)

    out = P+D+I
    return out

system = ([1.0], [1.0, 2.0, 1.0])
t, y = signal.impulse2(system)
plt.plot(t, y,'bo')


for i in range(len(t)):
    
    pid = PID(5,0,0,0.37,y[i])
    plt.plot(t[i],pid,'ro')




#plt.step(t, 250)
plt.show()