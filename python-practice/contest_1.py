lst = []
c = int(input())
count = 0

for i in range(2):
    lst.append([int(num) for num in input().split()])
for i, j in enumerate(lst):
    if len(j) > c:
        lst[i] = j[:c]
    # print(lst)


for row, i in enumerate(lst):
    for col, j in enumerate(i):
        if j == 1:
            count+=3
            # if col == 0 or col % 2 == 0:
            #     # lst[row][col - 1 if col > 0 else col] == 0 and lst[row - 1 if row > 0 else row][col] == 0 and
            #     if lst[row][col+1 if col < c-1 else col-1] == 0 and lst[row+1 if row < 1 else row-1][col] == 0:
            #         count += 3
            # else:
            #     if lst[row][col + 1 if col < c - 1 else col - 1] == 0 and lst[row + 1 if row < 1 else row - 1][col] == 0:
            #         count += 3
            # if lst[row][col+1 if col < c-1 else col-1] == 1: #and lst[row][col-1 if col > 0 else col] == 1 and col == 0 or col % 2 == 0:
            #     count += 1
            # else:
            #     count += 2
            #     if col != lst[row][0] and col != lst[row][-1]:

for row, i in enumerate(lst):
    for col, j in enumerate(i):
        if j == 1:
            # if lst[row][col + 1 if col < c - 1 else col] == 1:
            #     count -= 1
            if lst[row][col-1 if col > 0 else col+1] == 1:
                count -= 1
            if lst[row][col+1 if col < len(lst[row])-1 else col-1] == 1:
                count -= 1
            if col == 0 or col % 2 == 0:
                if lst[row+1 if row < 1 else row-1][col] == 1:
                    count -= 1
                elif lst[row-1 if row > 0 else row+1][col] == 1:
                    count -= 1


print(count)
