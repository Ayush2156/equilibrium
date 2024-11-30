import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import PillowWriter
x = np.random.uniform(low=0, high=0.5, size=1000)
y = np.random.uniform(low=-0, high=1, size=1000)
points1= np.column_stack((x, y))
fig, axes = plt.subplots(2, 1, figsize=(10,6))
ax=axes[0]
lin1,=ax.plot([],[],'o',color='blue',ms=1)
ax.set_title("Box")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axvline(x=0.5, color='red', linestyle='--', linewidth=1)
ax.set_xticks([])
ax.set_yticks([]) 
ax=axes[1]
ax.set_title('graph counting particles in respective boxes')
ax.set_ylim(0,1000)
ax.set_xlim(0,600)
time_text = ax.text(0.65, 0.95, '', fontsize=15,bbox=dict(facecolor='white', edgecolor='black'), transform=ax.transAxes)

lin2,=ax.plot([],[],color='blue',label='No of particles in first part')
lin3,=ax.plot([],[],color='red',label='No of particles in second part')
ax.set_xlabel('Time[sec]')
ax.set_ylabel('numner of particles')
ax.grid('minor')
ax.legend(loc='upper right')
ax.axhline(y=500, color='green', linestyle='--', linewidth=1)
x_data = []
c1_data = []
c2_data = []
def animate(i):
 i1 = np.random.randint(0, len(points1))  # Random index
 r1= points1[i1]
 if r1[0]<0.5 :
   r1[0]=np.random.uniform(low=0.5,high=1)
   r1[1]=np.random.uniform(low=0,high=1)
   points1[i1]=r1
 else:
   r1[0]=np.random.uniform(low=0,high=0.5)
   r1[1]=np.random.uniform(low=0,high=1)
   points1[i1]=r1
 count1=points1[points1[:,0]<0.5]
 count2=points1[points1[:,0]>0.5]
 c1=len(count1)
 c2=len(count2) 
 x_data.append(i / 50)
 c1_data.append(c1)
 c2_data.append(c2)
 lin1.set_data(points1[:, 0], points1[:, 1])
 lin2.set_data(x_data,c1_data)
 lin3.set_data(x_data,c2_data)
 return lin1, lin2,lin3, time_text
ani = animation.FuncAnimation(fig, animate, frames=2000, interval=50)
ani.save('chemicalequilirium.gif',writer='pillow',fps=50,dpi=100)

