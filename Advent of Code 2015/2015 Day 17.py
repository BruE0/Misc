# Advent of Code 2015. Day 17#
#
#

from itertools import combinations

with open("santa.txt", "r") as f:
    containers = list(map(int, f.read().splitlines())) 

lst = []
for r in range(len(containers)):
    count = sum(150==sum(perm) for perm in combinations(containers,r))
    if count != 0:
        lst.append((r,count))

print(sum(x[1] for x in lst))
print(lst[0][1])

