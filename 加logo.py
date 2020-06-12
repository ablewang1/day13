from PIL import Image,ImageFilter

img = Image.open('image/a2.jpg')

logo = Image.open('image/a0.jpg')

logo = logo.resize((100,100),resample=Image.ANTIALIAS)

img.paste(logo,(30,150))
img.show()