from figures.figure import *


class Rook(Figure):
    def get_char(self):
        return 'R'

    def valid_move(self, row, col, board):

        if self.row != row and self.col != col:
            return False

        if self.row == row and self.col != col:
            for i in range(1, abs(col - self.col)):
                if col > self.col:
                    if board.field[row][self.col + i] is not None:
                        return False
                if col < self.col:
                    if board.field[row][self.col - i] is not None:
                        return False

        if self.row != row and self.col == col:
            for i in range(1, abs(row - self.row)):
                if row < self.row:
                    if board.field[self.row - i][col] is not None:
                        return False
                if row > self.row:
                    if board.field[self.row + i][col] is not None:
                        return False
        if not self.valid_attack(row, col, board):
            return False
        return True

    def valid_attack(self, row, col, board):
        if board.field[row][col] is not None and self.color != board.field[row][col].color:
                return True
        elif board.field[row][col] is None:
            return True
        return False