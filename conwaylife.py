#!/usr/bin/env python3
"""
    conwaylife.py
    2019
    game of life using numpy/scipy.

    - loads a starting grid from txt file.
    - wait for input:
      > empty line to advance a certain step(default=1) of generations.
      > writing a number changes step.

"""


import numpy as np
from scipy.ndimage import convolve
import os


CLEAR = "cls" if os.name == "nt" else "clear"
NEIGHBOR_KERNEL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])


def live_or_die(nparray):
    count_around = convolve(nparray, NEIGHBOR_KERNEL, mode="constant")
    nparray = np.where(
        nparray == 1,
        np.where((count_around == 2) | (count_around == 3), 1, 0),
        np.where(count_around == 3, 1, 0),
    )
    return nparray


def drawboard(nparray):
    array_draw = np.where(nparray == 1, "#", " ")
    print(*["".join(row) for row in array_draw], sep="\n")


def loadboard(filename, live):
    with open(filename, "rb") as f:
        data = f.read().splitlines()

    nparray = np.vstack(np.frombuffer(line, dtype=np.uint8) for line in data)
    nparray = np.where(nparray == ord(live), 1, 0)
    return nparray


def main():
    house = loadboard("conwayboard.txt", live="#")
    generation = 0
    step = 1

    while True:
        os.system(CLEAR)

        for _ in range(step):
            house = live_or_die(house)
            generation += 1

        drawboard(house)

        answer = input(f"{generation:06d}>")
        if answer.isdigit():
            step = int(answer)


if __name__ == "__main__":
    main()
