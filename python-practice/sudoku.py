
sudoku = [[0, 0, 0, 0], [0, 0, 2, 0], [0, 1, 0, 0], [3, 0, 0, 4]]

def zero(sudoku):
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if value == 0:
                return [i, j]
    return False

def make_assumption(sudoku):
    zeros = zero(sudoku)
    if not zeros:
        return True
    else:
        row, col = zeros

    for i in range(1, len(sudoku[0])+1):
        if check(sudoku, i, row, col):
            sudoku[row][col] = i
            if make_assumption(sudoku):
                return True
    return False


def check(sudoku, num, row, col):
    for i in range(len(sudoku[0])):
        if sudoku[row][i] == num:
            return False

    for i in range(len(sudoku)):
        if sudoku[i][col] == num:
            return False
    return True

make_assumption(sudoku)
for i in range(len(sudoku)):
    print(sudoku[i])