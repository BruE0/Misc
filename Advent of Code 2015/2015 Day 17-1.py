# Advent of Code 2015. Day 17 Part 1#
#
#

from itertools import combinations


with open("santa.txt", "r") as f:
    containers = list(map(int, f.read().splitlines()))       #[20, 15, 10, 5, 5]

count = 0
for r in range(len(containers)-1):
    count += sum([ 150==sum(perm) for perm in combinations(containers,r) ]  )

print(count)
