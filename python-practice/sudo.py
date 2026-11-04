import sys
from copy import deepcopy

def get_variants(sudoku):
        variants = []
        for i, row in enumerate(sudoku):
            for j, value in enumerate(row):
                if not value:
                    row_values = set(row)  # значения в строке
                    column_values = set([sudoku[k][j] for k in range(9)])  # значения в столбце
                    # в каком квадрате 2x2 находится клетка? Координаты этого квадрата
                    sq_y = i // 3
                    sq_x = j // 3
                    square2x2_values = {
                        sudoku[sq_y * 3][sq_x * 3],
                        sudoku[sq_y * 3 + 1][sq_x * 3],
                        sudoku[sq_y * 3 + 2][sq_x * 3],
                        sudoku[sq_y * 3][sq_x * 3 + 1],
                        sudoku[sq_y * 3 + 1][sq_x * 3 + 1],
                        sudoku[sq_y * 3 + 2][sq_x * 3 + 1],
                        sudoku[sq_y * 3][sq_x * 3 + 2],
                        sudoku[sq_y * 3 + 1][sq_x * 3 + 2],
                        sudoku[sq_y * 3 + 2][sq_x * 3 + 2],
                    }
                    exists = row_values | column_values | square2x2_values
                    values = set(range(1, 10)) - exists  # какие значения остались?
                    variants.append((i, j, values))
        return variants


def solve_sudoku(sudoku):
        if all([k for row in sudoku for k in row]):  # Если судоку заполнено, это ответ
            return sudoku

        variants = get_variants(sudoku)  # Иначе посмотрим все варианты
        print(variants)

        x, y, values = min(variants, key=lambda x: len(x[2]))  # Выберем тот, у которого меньше всего возможностей.
        for v in values:  # Попробуем все по очереди
            new_sudoku = deepcopy(sudoku)
            new_sudoku[x][y] = v
            s = solve_sudoku(new_sudoku)  # Если оно решилось, возвратим ответ.
            if s:
                return s


sudoku = [[int(i) for i in list(row)] for row in sys.stdin.read().split() if row]
print(sudoku)
print("\n".join(["".join([str(i) for i in row]) for row in solve_sudoku(sudoku)]))

# print(any([1, 0, 0]))

# 1 0 0 4 8 9 0 0 6
# 7 3 0 0 0 0 0 4 0
# 0 0 0 0 0 1 2 9 5
# 0 0 7 1 2 0 6 0 0
# 5 0 0 7 0 3 0 0 8
# 0 0 6 0 9 5 7 0 0
# 9 1 4 6 0 0 0 0 0
# 0 2 0 0 0 0 0 3 7
# 8 0 0 5 1 2 0 0 4