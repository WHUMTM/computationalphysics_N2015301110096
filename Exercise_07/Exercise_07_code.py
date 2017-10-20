import numpy as np    
import math
import mpl_toolkits.mplot3d 
import matplotlib.pyplot as plt

class BASEBALL(object):
    def __init__(self, _v0, theta, _vz0, _dt= 0.1, _omgx=0, _omgy=0, _omgz= 0):
        self.vx, self.vy, self.vz= _v0*math.cos(theta), _v0*math.sin(theta), _vz0 
        self.theta = theta
        self.v = _v0
        self.B2= 0.0039+ 0.0058/(1.+math.exp((self.v-35)/5))
        self.S0= 4.1E-4
        self.g= 9.8
        self.dt= _dt 
        self.x, self.y, self.z= [0], [1.8], [0]
        self.omgx = _omgx
        self.omgy = _omgy
        self.omgz = _omgz
    def calculate(self):
        while True: 
            self.x.append(self.vx*self.dt+self.x[-1])            # append coordinates to x,y,z
            self.y.append(self.vy*self.dt+self.y[-1])
            self.z.append(self.vz*self.dt+self.z[-1])       
            self.vx, self.vy, self.vz = \
                (-self.B2*self.v*self.vx)*self.dt+ self.vx+ self.S0 * (self.omgy*self.vz - self.omgz*self.vy) * self.dt, \
                (-self.g- self.B2*self.v*self.vy)*self.dt+ self.vy+ self.S0 * (self.omgz*self.vx - self.omgx*self.vz) * self.dt,\
                ( self.vz+ self.S0 * (self.omgx*self.vy - self.omgy*self.vx) * self.dt     )                # change the velocity           
            self.v= math.sqrt(self.vx**2+self.vy**2+self.vz**2)
            self.B2= 0.0039+ 0.0058/(1+math.exp((self.v-35)/5))
            if self.y[-1]< 0: 
                break
    def graphics1(self,_gra):
        _gra.plot(self.x, self.y, linestyle='-', linewidth=1.0, label='firing angle:%d'%(40+3*j) + r'$^{\circ}$')
            # plot the trajetory
    def graphics2(self,_gra):
    
        _gra.plot(self.x, self.y,label=r'$\omega$=%.f r/s'%(100*i) )  
    def graphics3(self,_gra):
        _gra.plot(self.x, self.z,label=r'$\omega$=%.f r/s'%(100*i) )
  
    def graphics(self,_gra, _omgz):             # plot the trajetory
        _gra.plot(self.z, self.x, self.y, label=r'$\omega$=%.f r/s'%_omgz)
        _gra.scatter([self.z[0],self.z[-1]],[self.x[0],self.x[-1]],[self.y[0],self.y[-1]],s=30)
       # _gra.text(self.z[-1], self.x[-1]-80, self.y[-1], r'$\omega$=%.f r/s'%_omgz,fontsize=10)


fig= plt.figure(figsize=(6,6))
ax3 = plt.subplot(1,1,1,projection='3d')
for omgz in [-200,-100,0,100,500]:          # change the angular velocity the determine the dependence of trajetory on omega
    comp= BASEBALL(49,49*np.pi/180,0,0.1,0,omgz,0)
    comp.calculate()
    comp.graphics(ax3, omgz)
    ax3.set_xlabel('z (m)', fontsize=18)
    ax3.set_ylabel('x (m)', fontsize=18)
    ax3.set_zlabel('y (m)', fontsize=18)
    #ax3.set_title('Trajectories of different $\omega_y$',fontsize=18)
    plt.legend(loc='center left', bbox_to_anchor=(0.8, 0.8))
 
plt.show(fig)

#FIGURE.1: draw a figure illustrating the deflection of each direction, just like fig.2.9 on the textbook


#FIGURE.2:Draw the 2D figure of various firing angles
ax = plt.subplot(1,1,1)
for j in range(6): 
    a = BASEBALL(55,(30+5*j)*np.pi/180,0,0.1,0,2000/60,0)
    a.calculate()
    a.graphics1(ax)
    #plt.plot(self.x, self.y, linestyle='-', linewidth=1.0, label='firing angle:%d'%(40+3*j) + r'$^{\circ}$')
plt.grid(True,color='k')
plt.title('placement and firing angles')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.ylim(0,70)
plt.legend(loc='upper right')
plt.show()



ax1=plt.subplot(211)

for i in [-10,0,1,2,4,5,15,50]:
    h=2
    b=BASEBALL(49,49*np.pi/180,0,0.1,0,100*i,0)
    b.calculate()
    b.graphics2(ax1)
plt.grid(True,color='k')
plt.title('motion curve of defferent $\omega_y$')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.ylim(0,60)

ax2=plt.subplot(212)
for i in [-10,0,1,2,4,5,15,50]:
    h=2
    b=BASEBALL(49,49*np.pi/180,0,0.1,0,100*i,0)
    b.calculate()
    b.graphics3(ax2)
plt.grid(True,color='k')

plt.xlabel('x (m)')
plt.ylabel('z (m)')


plt.legend(loc='center left', bbox_to_anchor=(1.1, 1))
plt.show()    

ax3=plt.subplot(211)

for i in [-10,0,1,2,4,5,15,50]:
    h=3
    b=BASEBALL(49,49*np.pi/180,0,0.1,0,0,100*i)
    b.calculate()
    b.graphics2(ax3)
plt.grid(True,color='k')
plt.title('motion curve of defferent $\omega_z$')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.ylim(0,70)

ax4=plt.subplot(212)
for i in [-10,0,1,2,4,5,15,50]:
    h=3
    b=BASEBALL(49,49*np.pi/180,0,0.1,0,0,100*i)
    b.calculate()
    b.graphics3(ax4)
plt.grid(True,color='k')
plt.xlabel('x (m)')
plt.ylabel('z (m)')
plt.legend()

plt.legend(loc='center left', bbox_to_anchor=(1, 1))
plt.show()    

ax5=plt.subplot(211)
for i in [-10,0,1,2,4,5,15,50]:
    h=1
    b=BASEBALL(49,49*np.pi/180,0,0.1,100*i,0,0)
    b.calculate()
    b.graphics2(ax5)
plt.grid(True,color='k')
plt.title('motion curve of defferent $\omega_y$')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.ylim(0,60)
ax6=plt.subplot(212)
for i in [-10,0,1,2,4,5,15,50]:
    h=1
    b=BASEBALL(49,49*np.pi/180,0,0.1,100*i,0,0)
    b.calculate()
    b.graphics3(ax6)
plt.grid(True,color='k')

plt.xlabel('x (m)')
plt.ylabel('z (m)')


plt.legend(loc='center left', bbox_to_anchor=(1, 1))
plt.show()    




