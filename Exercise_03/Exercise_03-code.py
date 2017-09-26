# programming to solve a freely falling objet(CH1 problem1.1) and provide a diagrammatic analysis
#@auther: WHUMTM, created on  Sep 25 2017, last modified on Sep 26 2017

#define the arrays 
V = [] 
t = []

#assign values to the constant
g = 9.8 
end_time = 10

#change the parameter
V_0=float(input('Initial velocity V0='))
dt=float(input('Please input time interval dt='))

#Initial value
t.append(0)
V.append(V_0)

#caculate
for i in range(int(end_time / dt)):
	Euler_ca = V[i] - g * dt
	V.append(Euler_ca)
	t.append(dt * (i + 1))

#draw the picture
import numpy as np
import matplotlib.pyplot as plt
plt.plot(t,V,'g')
plt.title('the velocity of a freely falling object')
plt.xlabel('t(s)')
plt.ylabel('V(m/s)')
plt.show()
savefig("Problem1.1.png")
