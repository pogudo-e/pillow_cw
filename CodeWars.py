import json
import urllib.request

from PIL import Image, ImageDraw, ImageFont


class CodeWars:
    def __init__(self, user_name):
        self.img = None
        self.total_completed = None
        self.leader_pos = None
        self.overall = None
        self.honor = None
        self.user_name = user_name

    def parse(self):
        dict_j = None
        try:
            url = f'https://www.codewars.com/api/v1/users/{self.user_name}'
            with urllib.request.urlopen(url) as response:
                body_json = response.read()
            dict_j = json.loads(body_json)
            if "success" in dict_j and dict_j["success"] == 0:
                raise ValueError("Request failed")
        except ValueError:
            print('Не загрузилось :(')
        self.honor = dict_j['honor']
        self.leader_pos = dict_j['leaderboardPosition']
        self.overall = dict_j['ranks']['overall']['name']
        self.total_completed = dict_j['codeChallenges']['totalCompleted']

    def draw(self):
        self.img = Image.open('src/img/pcw.png')

        i_draw = ImageDraw.Draw(self.img)
        handle = ImageFont.truetype('src/fonts/ubuntu_medium.ttf', size=32)
        i_draw.text((225, 12), text=str(self.user_name), font=handle, fill='#8C8C8C')  # имя пользователя
        handle_sub = ImageFont.truetype('src/fonts/ubuntu_medium.ttf', size=16)  # load font for sub text
        i_draw.text((113, 59), text=f'{self.honor}', font=handle_sub, fill='#D2D5D7')  # honor
        i_draw.text((227, 82), text=str(self.leader_pos), font=handle_sub, fill='#D2D5D7')  # leaderboard position
        i_draw.text((122, 106), text=str(self.overall), font=handle_sub, fill='#D2D5D7')  # overall
        i_draw.text((231, 130), text=str(self.total_completed), font=handle_sub, fill='#D2D5D7')  # total completed kata
        self.img.save('./src/output/canvas.png')

    def show(self):
        self.img.show()

    def draw_view(self):
        if self.img:
            self.img.show()
        else:
            print('Изображение не нарисовано!')

    def __str__(self):
        return (f'{self.user_name=}\n'
                f'{self.honor=}\n'
                f'{self.overall=}\n'
                f'{self.leader_pos=}\n'
                f'{self.total_completed=}\n')

    def __del__(self):
        self.img = None
        self.total_completed = None
        self.leader_pos = None
        self.overall = None
        self.honor = None
        self.user_name = None
