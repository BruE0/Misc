# Advent of Code 2015. Day 10#
#
#

from itertools import groupby, islice


def lookandsay(number='1', times=10):
    for _ in range(times+1):
        yield number
        number = ''.join(str(len(list(g))) + k
                         for k, g in groupby(number))


x = (islice(lookandsay('1113122113',50), 40, 51, 10))

print('40 times:',len(next(x)))
print('50 times:',len(next(x)))
