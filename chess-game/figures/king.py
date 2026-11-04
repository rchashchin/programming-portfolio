from figures.figure import *


class King(Figure):
    def get_char(self):
        return 'K'

    def valid_move(self, row, col, board):
        delta_row = abs(self.row - row)
        delta_col = abs(self.col - col)
        if max(delta_col, delta_row) == 1:
            if board.field[row][col] is None or board.field[row][col].color != self.color:
                return True
        return False

    def valid_attack(self, row, col, board):
        pass
