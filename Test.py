# Advent of Code 2015. Day 16 Part 2 #
#

from collections import defaultdict

with open("santa.txt", "r") as f:
    data = f.read().splitlines()

Sues = defaultdict(lambda: defaultdict(lambda: None))

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
        if Sues[index][things] == None:
            continue

        if things in ("pomeranians", "goldfish"):
            if Sues[index][things] >= MFCSAM[things]:
                FinalSues.remove(index)
                break

        elif things in ("cats", "trees"):
            if Sues[index][things] <= MFCSAM[things]:
                FinalSues.remove(index)
                break

        else:    
            if Sues[index][things] - MFCSAM[things] != 0:
                FinalSues.remove(index)
                break

print(FinalSues)
