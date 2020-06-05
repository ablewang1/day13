from PIL import Image,ImageFilter
from matplotlib import pyplot as plt
import os

path = os.listdir('image/')
# print(path)
c_path = os.getcwd()
print(os.getcwd())
os.chdir('image/')
print(os.getcwd())
plt.ion()
img_list = ["Hello"]
for i in path:
    plt.clf()
    img = Image.open(i)
    w,h = img.size
    print(w,h)
    # img = img.resize((400,400))
    # img.thumbnail((w//4,h//4))
    img.thumbnail((w*2,h*2))
    print(img.size)
    plt.imshow(img,alpha=1,resample=Image.ANTIALIAS)
    plt.pause(1)
    img = img.filter(ImageFilter.CONTOUR)
    plt.imshow(img)
    plt.pause(1)
    img = img.crop((10,10,200,200))  #抠图
    plt.imshow(img)
    plt.pause(1)
    img = img.rotate(45) #旋转
    plt.imshow(img)
    plt.title("Hi")
    plt.pause(1)
os.chdir(c_path)

plt.ioff()
plt.show()
