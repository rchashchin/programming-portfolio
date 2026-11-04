from board import *


def draw_board(board):
    print('       1    2    3    4    5    6    7    8')
    for row in range(7, -1, -1):

        print("    +----+----+----+----+----+----+----+----+")
        print(f'  {row + 1} ', end='')
        for col in range(8):
            if board.field[row][col] is None:
                print("|    ", end='')
            else:
                print(f'| {board.field[row][col].get_color()}{board.field[row][col].get_char()} ', end='')
        print('|')
    print("    +----+----+----+----+----+----+----+----+")
    print(f'Active: {board.active_player()}')
    start_row, start_col, end_row, end_col = map(int, input().split())
    board.move(start_row - 1, start_col - 1, end_row - 1, end_col - 1)


board = Board()


while True:

    draw_board(board)








