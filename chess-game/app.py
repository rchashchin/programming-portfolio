import pygame
import math
import os
from board import *

board = Board()

MESSAGES = {'check': 'Check!', 'checkmate': 'Checkmate!', 'stalemate': 'Stalemate!'}
# Draws one full frame of the game window:
#   - the checkered squares and every piece,
#   - orange highlights for legal target squares while a piece is held (next_moves=True),
#   - a gold square under the king plus the check message ('ШАХ!' is Russian for 'check') when in check,
#   - the grid lines, and a circle on the right showing whose turn it is.
# Finishes with pygame.display.flip() so the frame appears on screen.
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

    pygame.draw.rect(screen, pygame.Color('saddle brown'), ((820, 220), (120, 100)))

    if board.status in ('check', 'checkmate'):
        king_row, king_col = board.king_coords()
        pygame.draw.rect(screen, pygame.Color('goldenrod'), ((king_col * 100, king_row * 100), (100, 100)))
        characters(board, 'K', king_col, king_row)
    if board.status in MESSAGES:
        color = 'black' if board.field[king_row][king_col].color == 2 else 'white'
        text = font.render(MESSAGES[board.status], True, color)
        text_rect = text.get_rect(center=(870, 300))
        screen.blit(text, text_rect)

    for x in range(8):
        for y in range(8):
            pygame.draw.line(screen, pygame.Color('black'), (x * 100, 0), (x * 100, 800))
            pygame.draw.line(screen, pygame.Color('black'), (0, y * 100), (800, y * 100))

    pygame.draw.line(screen, pygame.Color('white'), (800, 0), (800, 800))
    pygame.draw.circle(screen, pygame.Color(board.active_player()), (875, 400), 70)
    pygame.display.flip()

# Highlights every square the held piece can legally move to, using board.check_move().
# It reads the module-level variables start_row/start_col (set when the mouse is pressed)
# and the global screen, then redraws the pieces so they stay on top of the highlights.
def show_next_moves(board, font_size = 30):
    for x in range(8):
        for y in range(8):
            # if board.field[start_row][start_col] is not None and board.field[start_row][start_col].valid_move(y, x, board) and \
            #         board.field[start_row][start_col].color == board.active and \
            if board.check_move(start_row, start_col, y, x) and board.field[start_row][start_col].color == board.active:
                pygame.draw.rect(screen, pygame.Color('orange2'), ((x * 100, y * 100), (100, 100)))
            if board.field[y][x] is not None:
                characters(board, board.field[y][x].get_char(), x, y)

PIECE_NAMES = {'P': 'pawn', 'R': 'rook', 'k': 'knight', 'B': 'bishop', 'Q': 'queen', 'K': 'king'}
IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imgs')
PIECE_SIZE = 80          # squares are 100x100, so this leaves a margin
_image_cache = {}


# Returns the scaled image for one piece type and colour (color 1 = white, 2 = black).
# The PNG is loaded and resized the first time only, then stored in _image_cache for reuse.
def get_piece_image(color, char):
    key = (color, char)
    if key not in _image_cache:
        prefix = 'w' if color == 1 else 'b'
        path = os.path.join(IMG_DIR, f'{prefix}_{PIECE_NAMES[char]}.png')
        image = pygame.image.load(path).convert_alpha()
        width, height = image.get_size()
        scale = PIECE_SIZE / max(width, height)
        _image_cache[key] = pygame.transform.smoothscale(image, (int(width * scale), int(height * scale)))
    return _image_cache[key]

# Draws the piece at board square (x, y) onto the screen, centred in its 100x100 square.
# The name is left over from when it drew letters; it now draws the piece image.
# (The 'char' parameter picks the image; 'font_size' is no longer used.)
def characters(board, char, x, y, font_size=30):
    image = get_piece_image(board.field[y][x].color, char)
    rect = image.get_rect(center=(x * 100 + 50, y * 100 + 50))
    screen.blit(image, rect)
    
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
