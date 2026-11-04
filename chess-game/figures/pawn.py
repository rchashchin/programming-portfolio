from figures.figure import *


class Pawn(Figure):
    def get_char(self):
        return 'P'

    def valid_move(self, row, col, board):
        if self.color == WHITE:
            direction = 1
            start_position = 1
        else:
            direction = -1
            start_position = 6

        if self.row + direction == row \
                and self.col == col \
                and board.field[row][col] is None:
            return True

        if start_position == self.row \
                and self.row + 2 * direction == row \
                and self.col == col \
                and board.field[row][col] is None \
                and board.field[row-direction][col] is None:
            return True
        if self.valid_attack(row, col, board):
            return True
        return False


    def valid_attack(self, row, col, board):
        if board.field[row][col] is not None and self.color != board.field[row][col].color:
            if abs(self.row - row) == 1 and abs(self.col - col) == 1:
                if (self.color == WHITE and (row - self.row == 1 and abs(self.col - col) == 1)) or (self.color == BLACK and (self.row - row == 1 and abs(self.col - col) == 1)):
                    return True
        return False


