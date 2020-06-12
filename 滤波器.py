from PIL import Image,ImageFilter
from matplotlib import pyplot as plt
img = Image.open('image/a0.jpg')

img1 = img.filter(ImageFilter.CONTOUR) #轮廓
img2 = img.filter(ImageFilter.BLUR) #模糊
img3 = img.filter(ImageFilter.BoxBlur(radius=1)) #模糊
img4 = img.filter(ImageFilter.DETAIL) #锐化
img5 = img.filter(ImageFilter.EMBOSS) #浮雕
img6 = img.filter(ImageFilter.EDGE_ENHANCE) #边缘增强

# print(help(ImageFilter.BoxBlur))
# img.show()
fig = plt.figure(figsize=(300,100))
plt.subplot(161)
plt.imshow(img)
plt.subplot(162)
plt.imshow(img1)
plt.subplot(163)
plt.imshow(img2)
plt.subplot(164)
plt.imshow(img3)
plt.subplot(165)
plt.imshow(img4)
plt.subplot(166)
plt.imshow(img5)
plt.show()