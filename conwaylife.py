#!/usr/bin/env python3
"""
    conwaylife.py
    2018
    simple console based game of life using numpy.

    - loads a starting grid from txt file.
    - wait for input:
      > empty line to advance a certain step(default=1) of generations.
      > writing a number changes step.

"""


import numpy as np
import os


CLEAR_CONSOLE = "cls" if os.name == "nt" else "clear"


def count_around(nparray):
    '''Counts the number of cells alive around each cell.'''
    nparray = (np.roll(nparray, 1, axis=0) + np.roll(nparray, -1, axis=0) +
        np.roll(nparray, 1, axis=1) + np.roll(nparray, -1, axis=1) +
        np.roll(nparray, (1, 1), axis=(0, 1)) + np.roll(nparray, (-1, 1), axis=(0, 1)) +
        np.roll(nparray, (1, -1), axis=(0, 1)) + np.roll(nparray, (-1, -1), axis=(0, 1)) )
    nparray = np.pad(nparray[1:-1,1:-1], pad_width=1, mode='constant', constant_values=0)
    return nparray


def live_or_die(nparray, count_around):
    '''Uses Conway's standard rules to check if a cell will live or die.'''
    nparray = np.where(nparray == 1, np.where((count_around == 2) | (
        count_around == 3), 1, 0), np.where(count_around == 3, 1, 0))
    return nparray


def drawboard(nparray):
    array_draw = np.where(nparray == 1, "#", " ")
    print("\n".join([''.join(row) for row in array_draw]))


def loadboard(filename, live="1"):
    with open(filename, "rb") as f:
        data = f.read().splitlines()

    nparray = np.vstack([np.frombuffer(line, dtype=np.uint8) for line in data])
    nparray = np.where(nparray == ord(true), 1, 0)
    nparray = np.pad(nparray, pad_width=1, mode='constant', constant_values=0)
    return nparray



def main():
    house = loadboard("conwayboard.txt", live="#")
    generation = 0
    step = 1

    while True:
        os.system(CLEAR_CONSOLE)

        for _ in range(step):
            around = count_around(house)
            house[1:-1,1:-1] = live_or_die(house[1:-1,1:-1],around[1:-1,1:-1])
            generation += 1

        drawboard(house[1:-1,1:-1])

        answer = input(f"{generation:06d}>")
        if answer.isdigit():
            step = int(answer)


if __name__ == "__main__":
    main()
