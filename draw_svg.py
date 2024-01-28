import svgwrite


class Draw_svg:
    def __init__(self):
        self.font_family = None
        self.font_weight = None
        self.font_size = None
        self.fill = None
        self.text = None
        self.view_box = None

    def text_draw(self):
        dwg.add(dwg.text(f'{self.text}',
                         insert=(50, 180),
                         stroke='#500',
                         fill=f'{self.fill}',
                         stroke_width=2,
                         font_size=f'{self.font_size}',
                         font_weight=f"{self.font_weight}",
                         font_family=f"{self.font_family}"))


dwg = svgwrite.Drawing('text.svg', profile='tiny')
dwg.viewbox(width=400, height=180)
rectangle = dwg.rect(insert=(0, 0), size=(400, 180), rx=5, ry=5, fill='#1C1C1E')
dwg.add(rectangle)

dwg.add(
    dwg.circle(center=(25, 23),
               r=10,
               fill='#D2D5D7'))
dwg.add(
    dwg.text('CodeWars/', insert=(45, 32), fill='#D2D5D7', font_size='26px', font_weight='bold', font_family='Ubuntu'))
dwg.add(
    dwg.text('Pogudo', insert=(185, 32), fill='#8C8C8C', font_size='26px', font_weight='bold', font_family='Ubuntu'))

dwg.save()
