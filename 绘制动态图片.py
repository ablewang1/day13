from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# x = [-5,5,-3,0,3,-5]
# y = [5,5,-7,10,-7,5]
# plt.plot(x,y,c='r')
x = np.linspace(-5,6,20)
y1 = 4 + np.random.rand(20)
plt.ion()
b = ['w','b','r','g','c','m','y','k']
for i in range(2,500):
    for j in b:
        plt.cla()
        plt.scatter(x,y1,c=j,s=i)
        plt.pause(0.1)
plt.ioff()
plt.show()
# plt.scatter(x,y1)
# plt.show()