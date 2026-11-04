from itertools import *

n = int(input())
data = {}
for i in range(n):
    info = [int(i) for i in input().split()]
    data[info[0]] = info[1]
dif = 0
speed = 0
time_dif = 0
best_speed = 0
for i in permutations(data, 2):
    dif = 0
    speed = 0
    time_dif = 0
    # print(i)
    if data[i[0]] < data[i[1]]:
        dif = data[i[1]] - data[i[0]]
    else:
        dif = data[i[0]] - data[i[1]]
    if i[0] < i[1]:
        time_dif = i[1] - i[0]
    else:
        time_dif = i[0] - i[1]

    speed = dif/time_dif
    # print(speed)
    if speed > best_speed:
        best_speed = speed

print(best_speed)