from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
import torch
import numpy as np



fig = plt.figure()
ax = Axes3D(fig)
x = torch.rand(300)
y = torch.rand(300)
z = x**3+y**3
plt.ion()
b = ['w','b','r','g','c','m','y','k']
for i in range(2,500):
    plt.cla()
    for j in b:

        ax.scatter(x,y,z,c=j,s=i,marker='*')
        plt.pause(0.01)

plt.ioff()
plt.show()
