# Advent of Code 2015. Day 9#
#
# This code is currently considered level A / 10 danger. Read it at your own risk. You have been advised
#                    Spagetthiness = ***__
#      #                 Bad logic = ****_
#     # #          PEP8 compliance = _____
#    # ! #                    Eval = *****
#   #######                   Exec = XXXXXXXXXXXXXXXXXXXXXXXXXXXX

with open("santa.txt", "r") as f:
    data = f.read().splitlines()

gates = {"SET": "", "OR": "|", "AND": "&",
         "NOT": "~", "RSHIFT": ">>", "LSHIFT": "<<"}

code = []
for line in data:

    line = line.replace("is", "Castlevania_2")  # { fixing the pesky variable names
    line = line.replace("as", "iss")            #    in the input file
    line = line.replace(" if", " the")          #       >:(
    line = line.replace("in", "best_one")

    word = line.split(" ")
    if len(word) == 3:
        x, _, z = word
        GATE = "SET"
        y = ""
    elif word[1] in ("ANDORSHIFTLSHIFT"):
        x, GATE, y, _, z = word

    elif word[0] == "NOT":
        GATE, y, _, z = word
        x = ""

    code.append(f"{z} = {x} {gates[GATE]} {y}")

for _ in range(109):
    for line in code:
        try:
            exec(line)                           # exec executed 109 times.
        except (NameError, TypeError):           #  109 babies died because of this.
            continue

print(a)

# Answer for part 2 is obtained by literally going to the end of your input file,
#   "1674 -> b" is a few lines before the last one.
# change 1674 by the value you obtained in part 1 and do it again.
# YOLO Strats, brother.
