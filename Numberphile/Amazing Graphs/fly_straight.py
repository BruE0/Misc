#!/usr/bin/env python3
# fly_straight.py


import matplotlib.pyplot as plt
from math import gcd


def fly_straight(max_terms=10000):
    nums = [1, 1]
    for n in range(2, max_terms):
        gcdd = gcd(nums[-1], n)
        if gcdd == 1:
            nums.append(nums[-1] + n + 1)
        else:
            nums.append(nums[-1] // gcdd)
    return nums


fig, ax = plt.subplots(1)


ax.plot(fly_straight(1000), ".", markersize=3)

ax.minorticks_on()
ax.grid(True, which="both")
plt.show()
