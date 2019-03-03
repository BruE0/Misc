# Advent of Code 2015. Day 1 #
#

with open("santa.txt", "r") as f:
    line = f.readline()

print("Final floor:", line.count("(") - line.count(")"))


level = 0
for index,char in enumerate(line):
    if char == "(":
        level += 1
    elif char == ")":
        level -= 1
    else:
        raise SystemError("Expecting ( or ) characters only")

    if level < 0:
        print("First entering basement in level:",index)
        break
