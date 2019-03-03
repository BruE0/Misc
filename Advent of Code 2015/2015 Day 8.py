# Advent of Code 2015. Day 8#
#

import re

with open("santa.txt", "r") as f:
    data = f.read().splitlines()

def replace(line):
    line = re.sub(r'\\"', r'"',line)
    line = re.sub(r"\\\\",r"\\",line)
    line = re.sub(r'\\x[0-9a-f]{2}',r'X',line)
    return line

def encode(line):
    line = re.sub(r"\\",r"\\\\",line)
    line = re.sub(r'"', r'\\"',line)
    return line

print(sum( [len(line) - len(replace(line)[1:-1]) for line in data ] ))
print(sum( [2 + len(encode(line)) - len(line) for line in data ] ))