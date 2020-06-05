
from PIL import Image,ImageDraw
from matplotlib import pyplot as plt

fig = plt.figure(figsize=(50,50))
img = Image.open(r"image/b12.jpg")
plt.subplot(511)
plt.imshow(img)
log = Image.open(r"image/b11.jpg")
plt.subplot(512)
plt.imshow(log)
log = log.resize((90,90),resample=Image.ANTIALIAS)
plt.subplot(513)
plt.imshow(log)
img.paste(log,(50,50)) #加log
plt.subplot(514)
plt.imshow(img)
draw = ImageDraw.Draw(img)
draw.rectangle((10,10,50,50),outline=(0,255,0)) #框图
# img.show()
plt.subplot(515)
plt.imshow(img)
plt.show()
