# Advent of Code 2015. Day 4 #
#

import hashlib

data = "ckczppom"

First5 = True
for n in range(4000000):

    code = hashlib.md5(bytes(data + str(n), 'utf-8'))

    if code.hexdigest()[0:5] == "00000" and First5:
        print(f"{data}{n} starts with five zeros, therefore the answer is {n}")
        First5 = False
    if code.hexdigest()[0:6] == "000000":
        print(f"\n{data}{n} starts with SIX zeros, therefore the answer is {n}")
        break
