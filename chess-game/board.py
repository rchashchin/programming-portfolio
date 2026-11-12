import copy

from figures.__all__figures import *

def is_correct_coords(coords):
    return 0 <= coords[0] < 8 and 0 <= coords[1] < 8

class Board:
    def __init__(self):
        self.active = WHITE
        self.status = 'playing'
        self.field = [[None] * 8 for _ in range(8)]

        # Pawn
        self.field[1][1] = Pawn(WHITE, (1, 1))
        self.field[1][0] = Pawn(WHITE, (1, 0))
        self.field[1][2] = Pawn(WHITE, (1, 2))
        self.field[1][3] = Pawn(WHITE, (1, 3))
        self.field[1][4] = Pawn(WHITE, (1, 4))
        self.field[1][5] = Pawn(WHITE, (1, 5))
        self.field[1][6] = Pawn(WHITE, (1, 6))
        self.field[1][7] = Pawn(WHITE, (1, 7))
        self.field[6][1] = Pawn(BLACK, (6, 1))
        self.field[6][0] = Pawn(BLACK, (6, 0))
        self.field[6][2] = Pawn(BLACK, (6, 2))
        self.field[6][3] = Pawn(BLACK, (6, 3))
        self.field[6][4] = Pawn(BLACK, (6, 4))
        self.field[6][5] = Pawn(BLACK, (6, 5))
        self.field[6][6] = Pawn(BLACK, (6, 6))
        self.field[6][7] = Pawn(BLACK, (6, 7))
        self.field[6][1] = Pawn(BLACK, (6, 1))
        # Rook
        self.field[0][0] = Rook(WHITE, (0, 0))
        self.field[0][7] = Rook(WHITE, (0, 7))
        self.field[7][0] = Rook(BLACK, (7, 0))
        self.field[7][7] = Rook(BLACK, (7, 7))
        # Knight
        self.field[0][1] = Knight(WHITE, (0, 1))
        self.field[0][6] = Knight(WHITE, (0, 6))
        self.field[7][1] = Knight(BLACK, (7, 1))
        self.field[7][6] = Knight(BLACK, (7, 6))
        # Bishop
        self.field[0][2] = Bishop(WHITE, (0, 2))
        self.field[0][5] = Bishop(WHITE, (0, 5))
        self.field[7][2] = Bishop(BLACK, (7, 2))
        self.field[7][5] = Bishop(BLACK, (7, 5))
        # Queen
        self.field[0][3] = Queen(WHITE, (0, 3))
        self.field[7][3] = Queen(BLACK, (7, 3))
        # King
        self.field[0][4] = King(WHITE, (0, 4))
        self.field[7][4] = King(BLACK, (7, 4))

    # Plays a move from (start_row, start_col) to (end_row, end_col) for the active player.
    # Legality is decided by check_move(). If the move is rejected nothing changes and False is returned.
    # If it is allowed: the piece moves (capturing anything on the target), a pawn that reaches the last
    # row is promoted, the turn passes to the other player, the new status (check / checkmate /
    # stalemate) is worked out, and True is returned.
    def move(self, start_row, start_col, end_row, end_col):

        if not self.check_move(start_row, start_col, end_row, end_col):
            return False

        figure = self.field[start_row][start_col]

        self.change_figure(end_row, end_col, start_row, start_col)

            # if self.king_under_attack():
            #     self.change_figure(end_row, end_col, start_row, start_col)
            #     if self.king_under_attack():
            #         self.change_figure(start_row, start_col, end_row, end_col)
            #         return False
            # else:
            #     self.change_figure(end_row, end_col, start_row, start_col)

        if figure.get_char() == 'P' and ((self.active == WHITE and end_row == 7) or (self.active != WHITE and end_row == 0)):
            self.transform_pawn(end_row, end_col)
        self.next_player()
        self.update_status()
        return True

    def check_move(self, start_row, start_col, end_row, end_col):

        if not is_correct_coords((start_row, start_col)) or not is_correct_coords((end_row, end_col)):
            return False

        figure = self.field[start_row][start_col]

        if figure is None or figure.color != self.active:
            return False

        if not figure.valid_move(end_row, end_col, self):
            return False

        return not self.check_king_attacked(end_row, end_col, start_row ,start_col)

    def legal_moves(self):
        for start_row in range(8):
            for start_col in range(8):
                piece = self.field[start_row][start_col]
                if piece is not None and piece.color == self.active:
                    for end_row in range(8):
                        for end_col in range(8):
                            if self.check_move(start_row, start_col, end_row, end_col):
                                yield(start_row, start_col, end_row, end_col)

    def has_legal_move(self):
        return next(self.legal_moves(), None) is not None

    def update_status(self):
        in_check = self.king_under_attack(self.active)
        can_move = self.has_legal_move()
        if in_check and not can_move:
            self.status = 'checkmate'
        elif in_check:
            self.status = 'check'
        elif not can_move:
            self.status = 'stalemate'
        else:
            self.status = 'playing'

    def winner(self):
        if self.status != 'checkmate':
            return None
        return 'black' if self.active == WHITE else 'white'
    
    def active_player(self):
        return 'white' if self.active == WHITE else 'black'

    def transform_pawn(self, end_row, end_col):
        new_char = input(
            'What would you like your pawn to become?("R"-Rook/"k(small)"-Knight/"B"-Bishop/"Q"-Queen) ---  ')
        if new_char == "R":
            self.field[end_row][end_col] = Rook(self.active, (end_row, end_col))
        elif new_char == "k":
            self.field[end_row][end_col] = Knight(self.active, (end_row, end_col))
        elif new_char == "B":
            self.field[end_row][end_col] = Bishop(self.active, (end_row, end_col))
        elif new_char == "Q":
            self.field[end_row][end_col] = Queen(self.active, (end_row, end_col))

    def next_player(self):
        if self.active == WHITE:
            self.active = BLACK
        else:
            self.active = WHITE

    def change_figure(self, end_row, end_col, start_row, start_col):
        self.field[end_row][end_col] = self.field[start_row][start_col]
        self.field[end_row][end_col].row = end_row
        self.field[end_row][end_col].col = end_col
        self.field[start_row][start_col] = None

    def check_king_attacked(self, end_row, end_col, start_row, start_col):
        board2 = self.copy_board()
        mover_color = board2.field[start_row][start_col].color
        board2.change_figure(end_row, end_col, start_row, start_col)
        return board2.king_under_attack(mover_color)

    def copy_board(self):
        return copy.deepcopy(self)

    def find_king(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.field[row][col]
                if piece is not None and piece.color == color:
                        if piece.get_char() == 'K':
                            return row, col
    def king_coords(self):
            return self.find_king(self.active)

    def king_under_attack(self, color):
        king_row, king_col = self.king_coords()
        if king_row is None or king_col is None:
            return False
        for row in range(8):
            for col in range(8):
                piece = self.field[row][col]
                if piece is not None and piece.color != color:
                        if piece.valid_move(king_row, king_col, self):
                            return True
        return False


    # def next_move_king_under_attack(self, end_row, end_col):
    #     king_row, king_col = self.king_coords()
    #     # Нельзя двигать короля если следующая клетка под атакой
    #     for row in range(8):
    #         for col in range(8):
    #             if self.field[row][col] is not None:
    #                 if self.field[row][col].color != self.active:
    #                     if self.field[row][col].valid_move(end_row, end_col, self):
    #                         return True
    #     return False
 # нельзя двигать фигуры если ход оставляет короля без защиты в опасности
    


