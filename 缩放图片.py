from PIL import Image

img = Image.open('image/b12.jpg')
print(img.mode)
w,h =img.size
img1 = img.resize((1300,1300),resample=Image.ANTIALIAS) #返回一张修改后的图，不修改原图 #抗鋸齒

img1.show()
img2 = img.resize((1300,1300))
img2.show()
img.thumbnail((w//2,h//2),resample=Image.ANTIALIAS)  #对原图进行缩小
# img.show()

