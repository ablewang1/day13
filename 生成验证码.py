import random
from PIL import Image,ImageDraw,ImageFilter,ImageFont
import PIL

class GenerateCode():
    def __init__(self):
        self.code = []

    def get_code(self):
        code = chr(random.randint(65,90))
        self.code.append(code)
        return code

    def gb_color(self):
        return (random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255))

    def fr_color(self):
        return(random.randint(120,255),
               random.randint(120,255),
               random.randint(120,255))

    def ge_pic(self):
        w,h = 240,80
        img = Image.new(size=(w,h),mode="RGB",color=(255,255,255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font='Font/Arvo-Regular.ttf',size=50)

        for y in range(h):
            for x in range(w):
                draw.point((x,y),fill=self.gb_color())
        for i in range(4):
            draw.text((60*i+15,15),text=self.get_code(),fill=self.fr_color(),font=font)
            draw.rectangle((10,10,50,75),outline=(255,0,0))#画框
        # img.save('coid.jpg')
        img.show()

g = GenerateCode()
g.ge_pic()
print(g.code)

















# class GengrateCode():
#     def __init__(self):
#         self.code = []
#
#     def get_code(self):
#
#         b = chr(random.randint(65,90))
#         self.code.append(b)
#         return b
#
#     def bg_color(self):
#         return (random.randint(0,160),
#                 random.randint(0,160),
#                 random.randint(0,160))
#
#     def fr_color(self):
#         return (random.randint(120,255),
#                 random.randint(120,255),
#                 random.randint(120,255))
#
#     def ge_pic(self):
#         w,h = 240,80
#         img = Image.new(size=(w,h),mode="RGB",color=(255,255,255))
#         draw = ImageDraw.Draw(img)
#         font = ImageFont.truetype(font=r'Font/Arvo-Regular.ttf',size=50)
#
#         for y in range(h):
#             for x in range(w):
#                 draw.point((x,y),fill=self.bg_color())
#
#         for i in range(4):
#             draw.text((60*i+20,15),text=self.get_code(),fill=self.fr_color(),font=font)
#         print(self.code)
#         img = img.filter(ImageFilter.BLUR)
#         img.show()
#
#
# g = GengrateCode()
# g.ge_pic()







# class GenerateCode():
#
#     def getcode(self):
#         return chr(random.randint(65,90))
#
#     def bg_color(self):
#         return (random.randint(0,160),
#                 random.randint(0,160),
#                 random.randint(0,160))
#
#     def fr_color(self):
#         return (random.randint(120,255),
#                 random.randint(120,255),
#                 random.randint(120,255))
#
#     def gen_pic(self):
#
#         w,h = 240,60
#         img = Image.new(size=(w,h),mode="RGB",color=(255,255,255))
#         draw = ImageDraw.Draw(img)
#         font = ImageFont.truetype(font=r"Font/Arvo-Regular.ttf",size=30)
#
#         for y in range(h):
#             for x in range(w):
#                 draw.point((x,y),fill=self.bg_color())
#
#         for i in range(4):
#             draw.text((60*i+20,15),text=self.getcode(),fill=self.fr_color(),font=font)
#
#         img.show()
# g = GenerateCode()
# g.gen_pic()


