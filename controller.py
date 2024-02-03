from parser import Parser
from draw_png import Draw
from draw_svg import Draw_svg


class Controller:
    def __init__(self, user_name):
        self.parser = Parser(user_name)
        self.user = self.parser.get_user()
        self.draw = Draw(user_name)
        self.draw_svg = Draw_svg(user_name)

    def items(self, color):
        self.draw.color = color

    def paint(self):
        self.draw.draw()
        self.draw.add_text((113, 59), self.user.honor)
        self.draw.add_text((122, 106), self.user.ranks['overall']['name'])
        self.draw.add_text((227, 82), self.user.leaderboardPosition)
        self.draw.add_text((231, 130), self.user.codeChallenges['totalCompleted'])
        self.draw.img_save()

    def paint_svg(self, color):
        if not color: color = '#D2D5D7'
        self.draw_svg.settings(font_size='18px',
                               font_weight='bold',
                               font_family='Ubuntu',
                               fill=f'{color}',
                               fill_sub_text='#8C8C8C')
        self.draw_svg.draw(honor=f'{self.user.honor}',
                           overall=f'{self.user.ranks["overall"]["name"]}',
                           total=f'{self.user.codeChallenges["totalCompleted"]}')
        self.draw_svg.save()

    def __str__(self):
        return (f"{self.user.ranks['overall']['name']= }\n"
                f"{self.user.codeChallenges['totalCompleted']= }\n")


if __name__ == '__main__':
    test = Controller('Pogudo')
    print(test)
    test.paint()
