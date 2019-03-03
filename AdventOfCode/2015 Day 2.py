# Advent of Code 2015. Day 2 #
#

from itertools import combinations

with open("santa.txt", "r") as f:
    data = f.read().splitlines()

def wrapping(l,w,h):
    sides = [ x[0]*x[1] for x in combinations([l,w,h],2) ]
    return 2*sum(sides) + min(sides)

def ribbon(l,w,h):
    return l*w*h + 2*min(l+w, l+h, w+h)

print("Wrapping paper:", sum( [ wrapping(*map(int, line.split('x'))) for line in data] ))

print("Ribbon:", sum( [ ribbon(*map(int, line.split('x'))) for line in data] ))
