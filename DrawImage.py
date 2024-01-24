from PIL import Image, ImageDraw, ImageFont


class DrawImage:
    def __init__(self, user_name, honor, overall, leaderboard, total):
        self.img = Image.open('src/img/pcw.png')

        i_draw = ImageDraw.Draw(self.img)
        # idraw.rectangle((30, 30, 100, 100), fill='white')
        handle = ImageFont.truetype('src/fonts/ubuntu_medium.ttf', size=32)
        i_draw.text((225, 12), text=user_name, font=handle, fill='#8C8C8C')  # имя пользователя
        handle_sub = ImageFont.truetype('src/fonts/ubuntu_medium.ttf', size=16)  # load font for sub text
        i_draw.text((113, 59), text=str(honor), font=handle_sub, fill='#D2D5D7')  # honor
        i_draw.text((227, 82), text=str(leaderboard), font=handle_sub, fill='#D2D5D7')  # leaderboard position
        i_draw.text((122, 106), text=overall, font=handle_sub, fill='#D2D5D7')  # overall
        i_draw.text((231, 130), text=str(total), font=handle_sub, fill='#D2D5D7')  # total completed kata
        self.img.save('./src/output/canvas.png')

    def show(self):
        self.img.show()
