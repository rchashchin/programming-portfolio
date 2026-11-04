# Chess Game (Python)

A two-player chess game written in Python from scratch, with a console version and a graphical version built on `pygame`. Each piece is its own class, and the board handles turns, captures, and check detection.

## Features
- Object-oriented design: a `Figure` base class with `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, and `King` subclasses
- Legal-move validation per piece (blocked paths, captures, pawn movement)
- Turn tracking for white and black
- Check detection, and a rule that prevents moves that leave your own king in check
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
figures/        one file per piece type
```

## Known limitations / next steps
- Checkmate and stalemate are not detected yet
- Castling and en passant are not implemented
- A king can currently move into an attacked square (the check test uses the king's old position)
- The GUI draws letters instead of the piece images in `imgs/`
- Pawn promotion uses a console prompt, even in the GUI version

## What I learned
Designing a class hierarchy, separating game rules from display, and debugging move logic by comparing expected and actual board states.
