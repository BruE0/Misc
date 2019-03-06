# Advent of Code 2015. Day 19-1#
#
#

import re


with open("santa.txt", "r") as f:
    data = f.read().splitlines()

medlst = re.findall(r'[A-Z][a-z]*', data[-1])

Subs = {}


for index in range(len(data) - 2):
    word = data[index].split(" ")
    A = word[0]
    B = word[-1]
    Subs.setdefault(A, []).append(B)


stringset = set()

for index, chemical in enumerate(medlst):
    if chemical in Subs:
        for ii in range(len(Subs[chemical])):
            A = medlst.copy()
            A[index] = Subs[chemical][ii]
            stringset.add(''.join(A))

print(len(stringset))
