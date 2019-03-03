# Advent of Code 2015. Day 6 Part 2#
#

import numpy as np


def change(array, type, x0,y0,x1,y1):
    if type == "on":
        array[y0:y1+1, x0:x1+1] += 1
    elif type == "off":
        array[y0:y1+1, x0:x1+1] = np.where(array[y0:y1+1, x0:x1+1] > 0, array[y0:y1+1, x0:x1+1] - 1, 0)
    elif type == "toggle":
        array[y0:y1+1, x0:x1+1] += 2
    else:
        raise SystemError("Wrong change() type input.")
    return array

array = np.zeros((1000,1000))

with open("santa.txt", "r") as f:
    data = f.read().splitlines()

for line in data:
    mode, X, _, Y = line.replace("turn ","").split(" ")
    x0,y0 = X.split(",")
    x1,y1 = Y.split(",")
    array = change(array,mode,int(x0),int(y0),int(x1),int(y1))
    
print(np.sum(array))
