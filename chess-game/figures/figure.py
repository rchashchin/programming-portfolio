WHITE = 1
BLACK = 2


class Figure:
    def __init__(self, color, position):
        self.color = color
        self.row = position[0]
        self.col = position[1]

    def get_char(self):
        return 'X'

    def get_color(self):
        return 'W' if self.color == WHITE else 'B'


