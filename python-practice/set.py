# name = 'roman'
# roman_set = set(name)
#
# print(roman_set)
#
# name = 'ruslan'
# ruslan_set = set(name)
# print(ruslan_set)
# print(roman_set.intersection(ruslan_set))
# print(roman_set - ruslan_set)
# print(ruslan_set - roman_set)
# print(roman_set.union(ruslan_set))
# print(roman_set | ruslan_set)
# print(roman_set.difference(ruslan_set))
# print(ruslan_set.difference(roman_set))
# print(roman_set - ruslan_set)
# print(roman_set.symmetric_difference(ruslan_set))
# print(set(range(1, 5)))
#

x = '''1 0 0 4 8 9 0 0 6
7 3 0 0 0 0 0 4 0
0 0 0 0 0 1 2 9 5
0 0 7 1 2 0 6 0 0
5 0 0 7 0 3 0 0 8
0 0 6 0 9 5 7 0 0 
9 1 4 6 0 0 0 0 0
0 2 0 0 0 0 0 3 7 
8 0 0 5 1 2 0 0 4'''

for i in [('').join(row.split()) for row in (x.split('\n'))]:
    print(i)