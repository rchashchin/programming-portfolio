import random
import string


def palin_word(l):
    k = l // 2 if l % 2 == 0 else l // 2 + 1
    x = [random.choice(letters) for i in range(k)]
    if l % 2 == 0:
        return ('').join(x) + ('').join(x[::-1])
    else:
        return (''.join(x)) + ('').join(x[:k-1][::-1])


letters = list(string.ascii_lowercase)
rows, cols, poli_rows, poli_cols = map(int, input().split())
result = [[None] * cols for _ in range(rows)]

col_index = 0

for word in [palin_word(rows) for _ in range(poli_cols)]:
    index_lettert_word = 0
    for row in result:
        row[col_index] = word[index_lettert_word]
        index_lettert_word += 1
    col_index += 1


for row in range(poli_rows):
    row = result[row]
    for index in range(len(row)):
        if row[index]:
            row[-(index + 1)] = row[index]

for word in range(len(result)):
    for i in range(len(result[word])):
        if not result[word][i]:
            result[word][i] = random.choice(letters)

# if rows == poli_rows and poli_cols < poli_rows and cols <= 2:
#     print("IMPOSSIBLE")
words = ''
words_set = set()
words_set_col = set()
reversed_list = []



for word in result:
    words = ('').join(word)
    words_set.add(words)
    reversed_list.append(words)

temporary = list(zip(*reversed_list))
for i in temporary:
    words_set_col.add(('').join(i))
# print(temporary)
# print(words_set)
if rows <= 1 and cols <= 1:
    print('IMPOSSIBLE')
elif len(words_set) != rows or len(words_set_col) != cols:
    print('IMPOSSIBLE')
else:
    for word in reversed_list:
        print(word)

# def create_rows(inp):
#     rows = []
#     for i in range(inp[0]-inp[2]):
#         word = ''.join(random.choice(letters) for _ in range(inp(1)))
#         rows.append(word)
#     for n in range(inp(2)):
#         palindrome = polin_word(inp(0))
#         rows.append(palindrome)
#     random.shuffle(rows)
#     return rows
#
# def create_final(inp):
#     # final = []
#     for n in range(inp[0]):
#         final = create_rows(inp)
#         # final.append(row)
#     for m in range(inp[1]):
#         pass

# print(palin_word(inp))





