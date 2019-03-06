# Advent of Code 2015. Day 18#
#
#

import numpy as np

with open("santa.txt", "rb") as f:
    data = f.read().splitlines()

house = np.vstack([np.frombuffer(line, dtype=np.uint8) for line in data])
house = np.where(house < 46, 1, 0)
house = np.pad(house, pad_width=1, mode='constant', constant_values=0)

house2 = house.copy()

def count_around(nparray):
    nparray = np.roll(nparray, 1, axis=0) + np.roll(nparray, -1, axis=0) + \
        np.roll(nparray, 1, axis=1) + np.roll(nparray, -1, axis=1) + \
        np.roll(nparray, (1, 1), axis=(0, 1)) + np.roll(nparray, (-1, 1), axis=(0, 1)) + \
        np.roll(nparray, (1, -1), axis=(0, 1)) + np.roll(nparray, (-1, -1), axis=(0, 1))
    nparray = np.pad(nparray[1:-1,1:-1], pad_width=1, mode='constant', constant_values=0)
    return nparray


def live_or_die(nparray, count_around):
    nparray = np.where(nparray == 1, np.where((count_around == 2) | (
        count_around == 3), 1, 0), np.where(count_around == 3, 1, 0))
    return nparray


for _ in range(100):
    around = count_around(house)
    house[1:-1] = live_or_die(house[1:-1],around[1:-1])

print(f"Number of lights on: {np.sum(house)}")


house2[[1,1,-2,-2],[1,-2,1,-2]] = 1
for _ in range(100):
    around = count_around(house2)
    house2[1:-1] = live_or_die(house2[1:-1],around[1:-1])
    house2[[1,1,-2,-2],[1,-2,1,-2]] = 1

print(f"Number of lights on with 4 lights stuck: {np.sum(house2)}")
