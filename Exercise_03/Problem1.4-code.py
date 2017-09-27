# programming to solve a radioactive deacay problem involving two types of nuclei(CH1 problem1.4) and provide a diagrammatic analysis
#@auther: WHUMTM, created on  Sep 25 2017, last modified on Sep 27 2017


import math

#define the arrays 
time=[]
NA=[]
NB=[]
analysis_NA=math_NA=[]
analysis_NB=math_NB=[]


#assign values to the parameter
A0=A=100
tau_A=1
t=0
print('Program constant')
print('initial number of nuclei N_A(0)=100')
print('decay time constant for nuclei A tau_A/seconds =1')

#change the parameter
print('Please enter the following variables')
B0=B=float(input('initial number of nuclei N_B(0)='))
tau_B=float(input('decay time constant for nuclei B tau_ B/seconds(it canot be 1&0)='))
time_interval=float(input('time_interval dt/seconds(non-zero)='))
final_time=float(input('final_time/seconds='))


#Initial value
time.append(t)
NA.append(A)
NB.append(B)
math_NA.append(A0*math.exp(-t))
math_B=tau_B*A0*math.exp(-t)/(tau_A-tau_B)+(B0-tau_B*A0/(tau_A-tau_B))*math.exp(-t/tau_B)
math_NB.append(math_B)


#caculate
for i in range(int(final_time/time_interval)+1):
    t=time[i]+time_interval
    EULER_B=NB[i]+(NA[i]/tau_A-NB[i]/tau_B)*time_interval
    EULER_A=NA[i]-(NA[i]/tau_A)*time_interval 
    time.append(t)
    NA.append(EULER_A)
    NB.append(EULER_B)
    math_NA.append(A0*math.exp(-t))
    math_B=tau_B*A0*math.exp(-t)/(tau_A-tau_B)+(B0-tau_B*A0/(tau_A-tau_B))*math.exp(-t/tau_B)
    math_NB.append(math_B)

#draw the picture
import numpy as np
import matplotlib.pyplot as plt

#define the figure
fig, ax = plt.subplots()


#set lines
line1, = ax.plot(time, NA, '-', linewidth=3, 
                 label='Analytical solution $N_A$')
line2, = ax.plot(time, NB, '-', linewidth=3,
                 label='Simulation data $N_B$')
line3, = ax.plot(time,math_NA, '--', linewidth=2, 
                 label='Analytical solution $N_A$')
line4, = ax.plot(time,math_NB, '--', linewidth=2,
                 label='Simulation data $N_B$')


#insert legend
ax.legend(loc='upper right')

#add mesh
ax.grid(True,color='k')

#label the title and axis
ax.set_title('The Number of $N_A$ and $N_B$ ')
ax.set_xlabel('time (s)')
ax.set_ylabel('number of The Nuclei')
plt.show()
