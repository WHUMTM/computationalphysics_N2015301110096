import math
import matplotlib.pyplot as plt
import numpy as np      
from matplotlib import animation   
 
#calculate the trajectory
def Trajectory_cor(v,theta,B,T0):
    v_x=v * math.cos(theta * math.pi/180)
    v_y=v * math.sin(theta * math.pi/180)
    dt,y0,a,alpha=0.005,10**4,6.5*10**(-3),2.5
    x,y,t=0,0,0
    distance=[[]for i in range(3)]
    distance[0].append(x)
    distance[1].append(y)
               #negative for isothermal approximation
       #non-negative for adiabatic approximation
    def rho(height):
        return (1-a*height/T0)**alpha
    while y>= 0:
        a_x3, a_y3=-B*rho(y)*v*v_x,-9.8-B*rho(y)*v*v_y
        x=x+v_x*dt
        v_x=v_x+a_x3*dt
        y=y+v_y*dt
        v_y=v_y+a_y3*dt
        t=t+dt
        v=(v_x**2+v_y**2)**0.5
        distance[0].append(x/1000)   #divided by 1000 to change the unit from "meter" to "kilometer"
        distance[1].append(y/1000)
    distance[2].append(t)
    return distance
# plot
velocity=700
B=4*10**(-5)
T0=300

for i in range(2):
    angle=-i*10+45
    d=Trajectory_cor(velocity,angle,B,T0)
    plt.plot(d[0],d[1],linestyle='-',linewidth=1.0,label=angle)
    print (angle,d[0][-1],d[2][0])  
    
def Trajectory_uncor(v,theta,B):
    v_x=v * math.cos(theta * math.pi/180)
    v_y=v * math.sin(theta * math.pi/180)
    dt=0.005
    x,y,t=0,0,0
    distance=[[]for i in range(3)]
    distance[0].append(x)
    distance[1].append(y)
    while y>= 0:
        a_x2, a_y2=-B*v*v_x,-9.8-B*v*v_y
        x=x+v_x*dt
        v_x=v_x+a_x2*dt
        y=y+v_y*dt
        v_y=v_y+a_y2*dt
        t=t+dt
        v=(v_x**2+v_y**2)**0.5
        distance[0].append(x/1000)
        distance[1].append(y/1000)
    distance[2].append(t)
    return distance


#plot the figure for various angles
velocity=700
B=4*10**(-5)
for i in range(2):
    angle=-i*10+45
    d_1=Trajectory_uncor(velocity,angle,B)
    plt.plot(d_1[0],d_1[1],linestyle=':',linewidth=1.0,label=angle)
    print (angle,d[0][-1],d[2][0])

plt.xlim(0,30)
plt.ylim(0,10)
plt.title('Trajectory of Cannon Shell ')
plt.xlabel(' x(km)')
plt.ylabel(' y(km)')
plt.text(19,6.8,'With density correction')
plt.text(8.5,1.5,'Without density correction')

with plt.xkcd():
     plt.annotate(
        '',
        xy=(21.8, 4), arrowprops=dict(arrowstyle='->'), xytext=(25.1, 6.5))
     plt.annotate(
        '',
        xy=(20.5, 3.3), arrowprops=dict(arrowstyle='->'), xytext=(22, 6.5))
     plt.annotate(
        '',
        xy=(17.8, 3.8), arrowprops=dict(arrowstyle='->'), xytext=(11, 2.1))
     plt.annotate(
        '',
        xy=(19.4, 3.4), arrowprops=dict(arrowstyle='->'), xytext=(13, 2.1))

plt.show()
