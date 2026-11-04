
from figures.figure import *


class Knight(Figure):
    def get_char(self):
        return 'k'

    def valid_move(self, row, col, board):
        delta_row = abs(self.row - row)
        delta_col = abs(self.col - col)

        if max(delta_col, delta_row) == 2 and min(delta_row, delta_col) == 1:
            if self.valid_attack(row, col, board):
                return True
        return False

    def valid_attack(self, row, col, board):
        if board.field[row][col] is not None and self.color != board.field[row][col].color:
            return True
        if board.field[row][col] is None:
            return True
        return False