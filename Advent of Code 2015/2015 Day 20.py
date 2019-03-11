# Advent of Code 2015. Day 20#
#
#

from functools import reduce
from math import sqrt

def factors(n):
        step = 2 if n % 2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if not n % i)))

for n in range(1,1000000):
    if sum(10*x for x in factors(n)) >= 29000000:
        print(f"Part 1 = {n}")
        break


for n in range(1,1000000):
    if sum(11*x for x in factors(n) if n//x <= 50) >= 29000000:
        print(f"Part 2 = {n}")
        break
