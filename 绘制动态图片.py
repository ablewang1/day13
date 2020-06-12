from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# x = [-5,5,-3,0,3,-5]
# y = [5,5,-7,10,-7,5]
# plt.plot(x,y,c='r')
# x = np.linspace(-5,6,20)
# y1 = 4 + np.random.rand(20)
# plt.ion()
# b = ['w','b','r','g','c','m','y','k']
# for i in range(2,500):
#     for j in b:
#         plt.cla()
#         plt.scatter(x,y1,c=j,s=i)
#         plt.pause(0.1)
# plt.ioff()
# plt.show()
# # plt.scatter(x,y1)
# # plt.show()

# #实时画图
# # # a = np.ones((3,5,3))
# # # print(a)
# # a = np.arange(10)
# # print(np.ndarray((2,5),order="C"))
# x = []
# y = []
# fig = plt.figure()
#
# plt.ion()
# for i in range(20):
#     x.append(i)
#     y.append(i**2)
#     fig.clf()
#     # plt.plot(x,y,'.')
#     plt.scatter(x,y)
#     plt.pause(0.1)
# plt.ioff()
# plt.show()

#制作图例
x = np.random.rand(100)
y = np.random.randn(100)
x1 = np.random.rand(100)
y1 = np.random.randn(100)
plt.scatter(x,y,label="first")
plt.scatter(x1,y1,label="second")
plt.legend()
plt.show()