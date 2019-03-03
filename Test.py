# Advent of Code 2015. Day 16 Part 1 #
#

from collections import defaultdict

with open("santa.txt", "r") as f:
    data = f.read().splitlines()

Sues = defaultdict(lambda: defaultdict(lambda: float('inf')))

for line in data:
    wordlst = line.replace(",", "").replace(":", "").split(" ")

    index = int(wordlst[1])

    for ind in range(len(wordlst)):
        if ind > 1 and ind % 2 == 0:
            Sues[index][wordlst[ind]] = int(wordlst[ind + 1])


MFCSAM = {"children": 3, "cats": 7, "samoyeds": 2, "pomeranians": 3,
          "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1}

PossibleSue = [*range(1,501)]
FinalSues = set(PossibleSue)

for index in PossibleSue:
    for things in MFCSAM:
        if Sues[index][things] - MFCSAM[things] not in (0, float('inf')):
                FinalSues.remove(index)
                break

print(FinalSues)
