# 2018
# test.py
# Shit Game Of Life

import numpy as np
import os

with open("shitgameoflife.txt", "rb") as f:
    data = f.read().splitlines()

house = np.vstack([np.frombuffer(line, dtype=np.uint8) for line in data])
house = np.where(house < 46, 1, 0)
house = np.pad(house, pad_width=1, mode='constant', constant_values=0)

def count_around(nparray):
    nparray = (np.roll(nparray, 1, axis=0) + np.roll(nparray, -1, axis=0) +
        np.roll(nparray, 1, axis=1) + np.roll(nparray, -1, axis=1) +
        np.roll(nparray, (1, 1), axis=(0, 1)) + np.roll(nparray, (-1, 1), axis=(0, 1)) +
        np.roll(nparray, (1, -1), axis=(0, 1)) + np.roll(nparray, (-1, -1), axis=(0, 1)) )
    nparray = np.pad(nparray[1:-1,1:-1], pad_width=1, mode='constant', constant_values=0)
    return nparray


def live_or_die(nparray, count_around):
    nparray = np.where(nparray == 1, np.where((count_around == 2) | (
        count_around == 3), 1, 0), np.where(count_around == 3, 1, 0))
    return nparray


def drawboard(nparray):
    for rows in nparray:
        for char in rows:
            print("#"*char+" "*(not char), end="")
        print()


generation = 0
step = 1

while True:

    os.system('cls' if os.name == "nt" else "clear")

    for _ in range(step):
        around = count_around(house)
        house[1:-1,1:-1] = live_or_die(house[1:-1,1:-1],around[1:-1,1:-1])
        generation += 1

    drawboard(house[1:-1,1:-1])
    answer = input(f"{generation:06d}>")
    if answer.isdigit():
        step = int(answer)

