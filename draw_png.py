from PIL import Image, ImageDraw, ImageFont


class Draw:
    def __init__(self, user_name):
        self.handle_sub = None
        self.i_draw = None
        self.img = None
        self.user_name = user_name

    def draw(self):
        self.img = Image.open('src/img/pcw.png')

        self.i_draw = ImageDraw.Draw(self.img)
        handle = ImageFont.truetype('src/fonts/ubuntu_medium.ttf', size=32)
        self.i_draw.text((225, 12), text=str(self.user_name), font=handle, fill='#8C8C8C')  # имя пользователя
        self.handle_sub = ImageFont.truetype('src/fonts/ubuntu_medium.ttf', size=16)  # load font for sub text

    def add_text(self, xy: tuple[float, float], text: str):
        self.i_draw.text(xy=xy, text=f'{text}', font=self.handle_sub, fill='#D2D5D7')

    def img_save(self):
        self.img.save('./src/output/canvas.png')

    def show(self):
        self.img.show()
