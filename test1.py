from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random

class GeneratorCode():
    def __init__(self):
        self.code = []
    def get_code(self):
        code = chr(random.randint(65,90))
        self.code.append(code)
        return code

    def gb_color(self):
        return (random.randint(0,200),
                random.randint(0,200),
                random.randint(0,200))

    def fr_color(self):
        return (random.randint(120,255),
                random.randint(120,255),
                random.randint(120,255))

    def get_pic(self):
        w,h = 240,60
        img = Image.new(size=(w,h),mode="RGB",color=(255,255,255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font=r'Font/Lobster-Regular.ttf',size=50)

        for y in range(h):
            for x in range(w):
                draw.point((x,y),fill=self.gb_color())

        for i in range(4):
            draw.text((55*i+15,2),text=self.get_code(),fill=self.fr_color(),font=font)
        draw.rectangle((13,13,55,55),outline=(255,0,0))
        # img = img.filter(ImageFilter.BoxBlur(radius=3))

        img.show()

g = GeneratorCode()
g.get_pic()
print(g.code)
