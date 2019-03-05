# Advent of Code 2015. Day 13-1#
#
#

from itertools import permutations

with open("santa.txt", "r") as f:
    data = f.read().splitlines()


People = {}

for lines in data:
    word = lines.split(" ")
    A = word[0]
    B = word[-1].rstrip(".")
    if word[2] == "gain":
        n = int(word[3])
    else:
        n = -int(word[3])
    People.setdefault(A,{})[B] = n


optimal = float('-inf')
for per in permutations(People):
    happiness = sum( People[A][B]+People[B][A] for A,B in zip(per[:-1],per[1:]) )
    happiness += People[per[0]][per[-1]] + People[per[-1]][per[0]]
    optimal = max(optimal, happiness)

print(optimal)
