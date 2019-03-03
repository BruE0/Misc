# Advent of Code 2015. Day 3 #
#

with open("santa.txt", "r") as f:
    line = f.readline()

def move(char,x,y):
    if char == ">":
        x += 1
    elif char == "<":
        x -= 1
    elif char == "^":
        y += 1
    elif char == "v":
        y -= 1
    return (x,y)

visited = {(0,0)}
x = y = 0

for index in range( 0, len(line), 1 ):
    x,y = move(line[index],x,y)
    visited.add((x,y))

print("#1: Number of houses visited:", len(visited))

visited = {(0,0)}
x = y = 0

for index in range( 0, len(line), 2 ):
    x,y = move(line[index],x,y)
    visited.add((x,y))

x = y = 0

for index in range( 1, len(line), 2 ):
    x,y = move(line[index],x,y)
    visited.add((x,y))

print("#2: Number of houses visited by Santa and his Robot:", len(visited))
