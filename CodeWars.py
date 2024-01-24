from parser import parse_json
from DrawImage import DrawImage


class CodeWars:
    def __init__(self, user_name):
        self.img = None
        self.total_completed = None
        self.leader_pos = None
        self.overall = None
        self.honor = None
        self.user_name = user_name

    def parse(self):
        (self.honor,
         self.leader_pos,
         self.overall,
         self.total_completed) = parse_json(self.user_name)

    def draw(self):
        self.img = DrawImage(self.user_name, self.honor, self.overall, self.leader_pos, self.total_completed)

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
