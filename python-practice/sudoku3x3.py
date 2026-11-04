from pprint import pprint
from copy import deepcopy
from random import shuffle
from time import clock

"""
Для всех клеток на основе ограничений 
возвращает список возможных чисел, например:
(0, 0, {2, 3, 4, 5, 6, 7, 8, 9})
(0, 1, {2, 3, 5, 6, 8, 9})
(0, 2, {2, 3, 4, 5, 6, 7, 8, 9})
(0, 3, {1, 3, 4, 5, 6, 7, 8, 9})
(0, 4, {1, 3, 4, 6, 7, 9})
(0, 5, {1, 3, 4, 5, 6, 7, 8, 9})
(0, 6, {1, 2, 4, 5, 6, 7, 8, 9})
(0, 7, {1, 2, 4, 5, 7, 8})
(0, 8, {1, 2, 4, 5, 6, 7, 8, 9})
(1, 0, {4, 5, 6, 7, 8, 9})
"""


def get_variants(sudoku):
    variants = []
    for i, row in enumerate(sudoku):
        for j, value in enumerate(row):
            if not value:
                # значения в строке
                row_values = set(row)
                # значения в столбце
                column_values = set([sudoku[k][j] for k in range(9)])
                # в каком квадрате 3x3 находится клетка?
                # Координаты этого квадрата
                sq_y = i // 3
                sq_x = j // 3
                square3x3_values = set([
                    sudoku[m][n]
                    for m in range(sq_y * 3, sq_y * 3 + 3)
                    for n in range(sq_x * 3, sq_x * 3 + 3)
                ])
                exists = row_values | column_values | square3x3_values
                # какие значения остались?
                values = set(range(1, 10)) - exists
                variants.append((i, j, values))

    return variants


def solve(sudoku):
    # Если судоку заполнено, это ответ
    if all([k for row in sudoku for k in row]):
        return sudoku

    # Иначе посмотрим все варианты
    variants = get_variants(sudoku)

    # Выберем тот, у которого меньше всего возможностей.
    x, y, values = min(variants, key=lambda x: len(x[2]))

    # Попробуем все по очереди
    for v in values:
        # deepcopy создает полную копию списка с учетом всех вложенностей
        new_sudoku = deepcopy(sudoku)
        new_sudoku[x][y] = v
        # Если оно решилось, возвратим ответ.
        s = solve(new_sudoku)
        if s:
            return s
    return None


s = clock()
pprint(
    solve([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 2, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 5, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 8, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]))
print('Затраченное время:', clock() - s, 'сек')