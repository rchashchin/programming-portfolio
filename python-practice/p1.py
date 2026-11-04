# num = int(input())
# lst = [[i for i in input()] for i in range(num)]
# count = 0
#
# def find(lst):
#     for j in range(len(lst[0])):
#         value = 'Y'
#         for n in lst[1:]:
#             if n[j] != value:
#                 break
#             else:
#                 return j + 1
#     return False
# print(find(lst))

# class Tumba:
#     def __init__(self):
#         self.boxes = {1:[], 2:[], 3:[]}
#
#     def add(self, obj, box):
#         if box in [1, 2, 3]:
#             self.boxes[box].append(obj)
#
#     def remove(self, box):
#         if box in [1, 2, 3]:
#             self.boxes[box].pop()
#
#
# tumb = Tumba()






import random

def generate_palindrome():
    letters = "abcdefghijklmnopqrstuvwxyz"
    first_half = ''.join(random.choice(letters) for _ in range(3))
    second_half = first_half[::-1]
    return first_half + second_half[1:]

def generate_row(num_palindromes):
    letters = "abcdefghijklmnopqrstuvwxyz"
    row = []
    for i in range(5 - num_palindromes):
        word = ''.join(random.choice(letters) for _ in range(5))
        row.append(word)
    for i in range(num_palindromes):
        palindrome = generate_palindrome()
        row.append(palindrome)
    random.shuffle(row)
    return row

def generate_table(num_rows, num_palindromes_per_row, num_palindromes_per_column):

    table = []
    for i in range(num_rows):
        row = generate_row(num_palindromes_per_row)
        table.append(row)
    # Transpose the table to get palindromes in columns
    transposed_table = list(map(list, zip(*table)))
    for j in range(num_palindromes_per_column):
        palindrome_column = transposed_table.pop(random.randint(0, 4 - j))
        for i in range(num_rows):
            table[i].append(palindrome_column[i])
    return table

# Example usage
table = generate_table(5, 3, 3)
for row in table:
    print(row)

