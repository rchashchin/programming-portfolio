m = int(input())
n = int(input())
lst = []

for i in range(m):
    lst.append([int(num) for num in input().split()])
num = lst[0][0]

def check(lst, num):
    possible = []
    variants = {}
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if (i+1) * (j+1) == num and len(lst) > i and len(lst[i]) > j:
                nums = [(i+1, j+1), (j+1, i+1)]
                for k in nums:
                    if len(k) == 2:
                        possible.append(k)
                    variants = set(possible)
                    # print(variants)

                    for p in variants:
                        print(p)
                        if (len(lst), len(lst[-1])) == p:
                            return 'yes'
                        else:
                            check(lst, lst[p[0]-1][p[1]-1])
    return 'no'

print(check(lst, num))
