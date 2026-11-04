import pygame
import math
from board import *

board = Board()

def draw_board_game(screen, board, next_moves, font_size=30):
    font = pygame.font.Font(None, font_size)

    for x in range(8):
        for y in range(8):
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, pygame.Color('bisque'), ((x * 100, y * 100), (100, 100)))
            else:
                pygame.draw.rect(screen, pygame.Color('saddle brown'), ((x * 100, y * 100), (100, 100)))
            if board.field[y][x] is not None:
                characters(board, board.field[y][x].get_char(), x, y)

    if next_moves:
        show_next_moves(board)
    if board.king_under_attack():
        king_row, king_col = board.king_coords()
        pygame.draw.rect(screen, pygame.Color('goldenrod'), ((king_col * 100, king_row * 100), (100, 100)))
        color = 'black' if board.field[king_row][king_col].color == 2 else 'white'
        # text1 = font.render('K', True, color)
        text2 = font.render('ШАХ!', True, color)
        # text_rect1 = text1.get_rect(center=(king_col * 100 + 50, king_row * 100 + 50))
        text_rect2 = text2.get_rect(center=(870, 300))
        # screen.blit(text1, text_rect1)
        screen.blit(text2, text_rect2)
        characters(board, 'K', king_col, king_row)

    else:
        pygame.draw.rect(screen, pygame.Color('saddle brown'), ((820, 220), (120, 100)))

    for x in range(8):
        for y in range(8):
            pygame.draw.line(screen, pygame.Color('black'), (x * 100, 0), (x * 100, 800))
            pygame.draw.line(screen, pygame.Color('black'), (0, y * 100), (800, y * 100))

    pygame.draw.line(screen, pygame.Color('white'), (800, 0), (800, 800))
    pygame.draw.circle(screen, pygame.Color(board.active_player()), (875, 400), 70)
    pygame.display.flip()

def show_next_moves(board, font_size = 30):
    for x in range(8):
        for y in range(8):
            # if board.field[start_row][start_col] is not None and board.field[start_row][start_col].valid_move(y, x, board) and \
            #         board.field[start_row][start_col].color == board.active and \
            if board.check_move(start_row, start_col, y, x) and board.field[start_row][start_col].color == board.active:
                pygame.draw.rect(screen, pygame.Color('orange2'), ((x * 100, y * 100), (100, 100)))
            if board.field[y][x] is not None:
                characters(board, board.field[y][x].get_char(), x, y)


def characters(board, char, x, y, font_size=30):
    font = pygame.font.Font(None, font_size)
    color = 'white' if board.field[y][x].color == 1 else 'black'
    text = font.render(char, True, color)
    text_rect = text.get_rect(center=(x * 100 + 50, y * 100 + 50))
    screen.blit(text, text_rect)

pygame.init()

size = height, weight = 950, 800
screen = pygame.display.set_mode(size=size)
font_size = 30
running = True
screen.fill(pygame.Color('saddle brown'))
next_moves = False
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_row, start_col = event.pos[1] // 100, event.pos[0] // 100
            next_moves = True

        if event.type == pygame.MOUSEBUTTONUP:
            next_moves = False
            end_row, end_col = event.pos[1] // 100, event.pos[0] // 100
            board.move(start_row, start_col, end_row, end_col)
            draw_board_game(screen, board, next_moves)

    draw_board_game(screen, board, next_moves)
    pygame.display.flip()

pygame.quit()
