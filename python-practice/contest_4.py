n, m = map(int, input().split())
info = {}
for i in range(m):
    start, end, length, cost = map(int, input().split())
    # info[start] = {'end': end, 'length': length, 'cost': cost}

    try:
        info[start].append({'end': end, 'length': length, 'cost': cost})
    except:
        info[start] = []
        info[start].append({'end': end, 'length': length, 'cost': cost})
print(info)

for station in range(1, n + 1):
    # print(info[station])
    for station_end in range(1, n + 1):
        if station in info.keys():

            for key, value in info[station].items():
                if station == station_end:
                    continue
                else:
                    for st in info[station]:
                        if station_end == st['end']:
                            print(f'start: {station}, end: {station_end}, {st["length"]}, {st["cost"]}')
                        else:
                            pass


# 5 7
# 1 2 15 1
# 2 4 9 9
# 5 2 5 6
# 4 5 4 4
# 4 3 3 7
# 1 3 2 7
# 1 4 2 1