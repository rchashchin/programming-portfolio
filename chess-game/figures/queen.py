from figures.figure import *


class Queen(Figure):
    def get_char(self):
        return 'Q'

    def valid_move(self, row, col, board):
        delta_row = abs(self.row - row)
        delta_col = abs(self.col - col)

        if delta_col == delta_row:
            if delta_col == delta_row:
                if row > self.row and col > self.col:
                    direction_row = 1
                    direction_col = 1
                elif row > self.row and col < self.col:
                    direction_row = 1
                    direction_col = -1
                elif row < self.row and col < self.col:
                    direction_row = -1
                    direction_col = -1
                elif row < self.row and col > self.col:
                    direction_row = -1
                    direction_col = 1
                for step in range(delta_row - 1):
                    # print(step, step * direction_row + direction_row, step * direction_col + direction_col)
                    if board.field[self. row + (step * direction_row + direction_row)][self.col + (step * direction_col + direction_col)] is not None:
                        return False
                if not self.valid_attack(row, col, board):
                    return False
                return True

        elif self.row != row and self.col != col:
            return False

        elif self.row == row or self.col == col:
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
        return False





    def valid_attack(self, row, col, board):
        if board.field[row][col] is not None and self.color != board.field[row][col].color:
                return True
        elif board.field[row][col] is None:
            return True
        return False