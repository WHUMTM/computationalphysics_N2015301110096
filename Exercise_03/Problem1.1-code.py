# programming to solve a freely falling objet(CH1 problem1.1) and provide a diagrammatic analysis
#@auther: WHUMTM, created on  Sep 25 2017, last modified on Sep 27 2017

#define the arrays 
V = [] 
t = []
analysis_V=math_V=[]

#assign values to the constant
g = 9.8 
end_time = 10
t_0=0

#change the parameter
V_0=float(input('Initial velocity V0='))
dt=float(input('Please input time interval dt='))

#Initial value
t.append(t_0)
V.append(V_0)
math_V.append(V_0)

#caculate
for i in range(int(end_time / dt)):
	 Euler_ca = V[i] - g * dt
	 V.append(Euler_ca)
	 t.append(t_0 + dt * (i + 1))
     math_ca=V_0 - g*t[i+1]
     math_V.append(math_ca)


#draw the picture
import numpy as np
import matplotlib.pyplot as plt

#define the figure
fig, ax = plt.subplots()

#set lines
line1, = ax.plot(t, math_V, '-', linewidth=4, 
                 label='Analytical solution')
line2, = ax.plot(t, V, '--', linewidth=3,
                 label='Simulation data')

#insert legend
ax.legend(loc='lower left')

#add mesh
ax.grid(True,color='k')

#label the title and axis
ax.set_title('the velocity of a freely falling object')
ax.set_xlabel('time (s)')
ax.set_ylabel('Velocity (m/s)')

plt.show()
