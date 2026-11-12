"""Tests for the chess rules (check, checkmate, stalemate, legal moves).

Run with:   python test_board.py        (or:   pytest test_board.py)

Squares are written in normal chess notation ('e2', 'g8'); sq() converts them to the
(row, col) numbers the Board uses (row 0 = white's back rank, col 0 = the a-file).
"""
import sys
import time

from board import *


def sq(name):
    """'e2' -> (1, 4)"""
    return int(name[1]) - 1, ord(name[0]) - ord('a')


def make_board(pieces, active=WHITE):
    """Build a board from a list like [(King, WHITE, 'e1'), (Rook, BLACK, 'e8')]."""
    board = Board()
    board.field = [[None] * 8 for _ in range(8)]
    for piece_class, color, square in pieces:
        row, col = sq(square)
        board.field[row][col] = piece_class(color, (row, col))
    board.active = active
    board.update_status()
    return board


def play(board, *moves):
    """Play moves like 'e2e4'; fails the test if one of them is rejected."""
    for text in moves:
        start, end = sq(text[:2]), sq(text[2:])
        assert board.move(*start, *end), f'move {text} was rejected'


def legal_from(board, square):
    """Set of squares (as row, col) that the piece on `square` can legally move to."""
    start = sq(square)
    return {(er, ec) for sr, sc, er, ec in board.legal_moves() if (sr, sc) == start}


def all_legal(board):
    """Set of every legal move as (start_square, end_square) tuples of (row, col)."""
    return {((sr, sc), (er, ec)) for sr, sc, er, ec in board.legal_moves()}


def targets(*squares):
    return {sq(s) for s in squares}


# ----------------------------------------------------------------------------- basics

def test_start_position():
    board = Board()
    assert board.status == 'playing'
    assert len(list(board.legal_moves())) == 20


def test_move_returns_true_and_switches_turn():
    board = Board()
    assert board.move(*sq('e2'), *sq('e4')) is True
    assert board.active == BLACK


def test_bad_moves_are_rejected_and_change_nothing():
    board = Board()
    assert board.move(*sq('e3'), *sq('e4')) is False      # empty square
    assert board.move(*sq('e7'), *sq('e5')) is False      # black piece on white's turn
    assert board.move(*sq('e2'), *sq('e5')) is False      # pawn cannot jump three squares
    assert board.move(0, 0, 0, 8) is False                # target off the board
    assert board.move(-1, 0, 0, 0) is False               # start off the board
    assert board.move(0, 9, 0, 0) is False               # start off the board
    assert board.active == WHITE
    assert len(list(board.legal_moves())) == 20


def test_copy_is_independent_and_trials_do_not_touch_the_game():
    board = Board()
    before = [(p.get_char(), p.color, p.row, p.col) for row in board.field for p in row if p]
    list(board.legal_moves())                              # runs many trial moves on copies
    after = [(p.get_char(), p.color, p.row, p.col) for row in board.field for p in row if p]
    assert before == after

    clone = board.copy_board()
    clone.change_figure(*sq('e4'), *sq('e2'))
    assert board.field[1][4] is not None and board.field[3][4] is None


# ----------------------------------------------------------------------------- check rules

def test_pinned_piece_cannot_move():
    # The white bishop on e2 shields its king from the rook on e8, so it may not move at all.
    board = make_board([(King, WHITE, 'e1'), (Bishop, WHITE, 'e2'),
                        (Rook, BLACK, 'e8'), (King, BLACK, 'a8')])
    assert legal_from(board, 'e2') == set()


def test_pinned_piece_may_move_along_the_pin():
    # A pinned rook can still slide along the e-file (and capture the attacker), but not sideways.
    board = make_board([(King, WHITE, 'e1'), (Rook, WHITE, 'e2'),
                        (Rook, BLACK, 'e8'), (King, BLACK, 'a8')])
    assert legal_from(board, 'e2') == targets('e3', 'e4', 'e5', 'e6', 'e7', 'e8')


def test_king_cannot_step_into_check():
    board = make_board([(King, WHITE, 'e1'), (Rook, BLACK, 'f8'), (King, BLACK, 'h8')])
    assert board.status == 'playing'
    assert legal_from(board, 'e1') == targets('d1', 'd2', 'e2')   # f1 and f2 are on the rook's file


def test_check_can_be_blocked_or_escaped():
    board = make_board([(King, WHITE, 'e1'), (Bishop, WHITE, 'f1'),
                        (Rook, BLACK, 'e8'), (King, BLACK, 'h8')])
    assert board.status == 'check'
    assert all_legal(board) == {
        (sq('e1'), sq('d1')), (sq('e1'), sq('d2')), (sq('e1'), sq('f2')),   # king steps off the file
        (sq('f1'), sq('e2')),                                               # bishop blocks on e2
    }


def test_check_can_be_resolved_by_capturing_the_attacker():
    board = make_board([(King, WHITE, 'e1'), (Pawn, WHITE, 'c2'),
                        (Knight, BLACK, 'd3'), (King, BLACK, 'h8')])
    assert board.status == 'check'
    assert all_legal(board) == {
        (sq('c2'), sq('d3')),                                               # pawn takes the knight
        (sq('e1'), sq('d1')), (sq('e1'), sq('d2')), (sq('e1'), sq('e2')), (sq('e1'), sq('f1')),
    }
    assert board.move(*sq('c2'), *sq('c3')) is False                       # ignores the check


def test_king_cannot_capture_a_protected_piece():
    board = make_board([(King, WHITE, 'e1'), (Queen, BLACK, 'e2'),
                        (Rook, BLACK, 'e8'), (King, BLACK, 'a8')])
    assert board.status == 'checkmate'
    assert (sq('e1'), sq('e2')) not in all_legal(board)


# ----------------------------------------------------------------------------- game endings

def test_fools_mate():
    board = Board()
    play(board, 'f2f3', 'e7e5', 'g2g4', 'd8h4')
    assert board.status == 'checkmate'
    assert board.winner() == 'black'
    assert list(board.legal_moves()) == []
    assert board.move(*sq('a2'), *sq('a3')) is False


def test_scholars_mate():
    board = Board()
    play(board, 'e2e4', 'e7e5', 'd1h5', 'b8c6', 'f1c4', 'g8f6', 'h5f7')
    assert board.status == 'checkmate'
    assert board.winner() == 'white'


def test_check_status_during_normal_play():
    board = Board()
    play(board, 'e2e4', 'f7f6', 'd1h5')
    assert board.status == 'check'           # queen on h5 attacks the black king along h5-e8
    assert board.winner() is None


def test_stalemate():
    board = make_board([(King, WHITE, 'f7'), (Queen, WHITE, 'g6'), (King, BLACK, 'h8')], active=BLACK)
    assert board.status == 'stalemate'
    assert not board.king_under_attack()
    assert list(board.legal_moves()) == []
    assert board.winner() is None


# ----------------------------------------------------------------------------- perft

def perft(board, depth):
    """Counts every sequence of legal moves `depth` plies long (a standard move-generator test)."""
    if depth == 1:
        return len(list(board.legal_moves()))
    total = 0
    for start_row, start_col, end_row, end_col in board.legal_moves():
        child = board.copy_board()
        child.change_figure(end_row, end_col, start_row, start_col)
        child.next_player()
        total += perft(child, depth - 1)
    return total


def test_perft_from_start_position():
    # Published values for standard chess. Castling, en passant and promotion cannot happen in the
    # first 3 plies, so this game must produce exactly the same numbers.
    board = Board()
    assert perft(board, 1) == 20
    assert perft(board, 2) == 400
    assert perft(board, 3) == 8902


# ----------------------------------------------------------------------------- runner

if __name__ == '__main__':
    tests = [(name, func) for name, func in sorted(globals().items())
             if name.startswith('test_') and callable(func)]
    failed = 0
    for name, func in tests:
        started = time.time()
        try:
            func()
            print(f'PASS  {name}  ({time.time() - started:.1f}s)')
        except AssertionError as error:
            failed += 1
            print(f'FAIL  {name}: {error}')
    print(f'\n{len(tests) - failed}/{len(tests)} tests passed')
    sys.exit(1 if failed else 0)
