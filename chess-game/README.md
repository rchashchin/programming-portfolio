# Chess Game (Python)

A two-player chess game written in Python from scratch, with a console version and a graphical version built on `pygame`. Each piece is its own class, and the board handles turns, captures, and check detection.

## Features
- Object-oriented design: a `Figure` base class with `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, and `King` subclasses
- Legal-move validation per piece (blocked paths, captures, pawn movement)
- Turn tracking for white and black
- Full check handling: a move is only legal if it leaves your own king safe, so pinned pieces stay put, kings cannot step into attack zone, and a player in check must block, capture the attacker, or move the king
- Checkmate and stalemate detection
- Pawn promotion
- Highlights the available moves while you hold a piece (GUI version)

## Run it

```bash
pip install -r requirements.txt   # only needed for the GUI version

python main.py    # console version: enter moves as "start_row start_col end_row end_col", e.g. 2 5 4 5
python app.py     # graphical version: click and drag a piece
```

Requires Python 3.8+.

## Project structure
```
board.py        Board class: setup, move handling, check detection
app.py          pygame GUI
main.py         console interface
test_board.py   tests for the rules
figures/        one file per piece type
imgs/           piece images used by the GUI
```

## Known limitations / next steps
- Castling is not implemented
- Pawn promotion uses a console prompt, even in the GUI version
- No draw rules yet

## What I learned
Designing a class hierarchy, separating game rules from display, and debugging move logic by comparing expected and actual board states.
