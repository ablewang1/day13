from PIL import Image

img = Image.open('image/a2.jpg')
img1 = img.crop((100,60,400,400))
# img.show()
img2 = img1.rotate(-45) #旋转
img2.show()