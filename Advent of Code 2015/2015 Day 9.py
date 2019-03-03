# Advent of Code 2015. Day 9#
#

from collections import defaultdict
from itertools import permutations

with open("santa.txt", "r") as f:
    data = f.read().splitlines()

places = defaultdict(lambda: defaultdict(None))

for lines in data:
    A, _, B, _, distance = lines.split(" ")
    places[A][B] = int(distance)
    places[B][A] = int(distance)

shortest = float('inf')
nonshortest = 0

for perm in permutations(places):
    total = sum( map( lambda x,y: places[x][y], perm, perm[1:] ) )
    shortest = min(shortest, total)
    nonshortest = max(nonshortest, total)

print(f"shortest = {shortest}\nlongest = {nonshortest}")

