# Advent of Code 2015. Day 21#
#
#

import re
from itertools import combinations, product, chain
from collections import defaultdict

BOSS = {'hp': 109, 'damage': 8, 'armor': 2} # puzzle input

with open("equipment.txt", "r") as f:
    data = f.read().splitlines()

weapon = defaultdict(lambda: defaultdict(int))
armor = defaultdict(lambda: defaultdict(int))
ring = defaultdict(lambda: defaultdict(int))
armor['No_armor'] = defaultdict(int)
ring['No_ring'] = defaultdict(int)

for line in data:
    words = re.split(r"\s{2,}", line)
    if words == [""]:
        continue
    if 'Weapon' in words[0]:
        dict_where = weapon
        continue
    elif 'Armor' in words[0]:
        dict_where = armor
        continue
    elif 'Ring' in words[0]:
        dict_where = ring
        continue
    dict_where[words[0]]['cost'] = int(words[1])
    dict_where[words[0]]['damage'] = int(words[2])
    dict_where[words[0]]['armor'] = int(words[3])

equipmentcomb_withrings = product(weapon, armor, ring, ring)
equipmentcomb_withoutring = product(weapon, armor)
equipmentcomb = chain(equipmentcomb_withoutring, equipmentcomb_withrings)

equipdict = {**weapon, **armor, **ring}

def player_win(attack, defense):
    damage_byplayer = attack - BOSS['armor']
    damage_byBOSS = BOSS['damage'] - defense
    if damage_byBOSS <= 0:
        return True
    elif damage_byplayer <= 0:
        return False
    return BOSS['hp'] / damage_byplayer <= 100 / damage_byBOSS + 1

minimum = float('inf')
maximum = 0

for comb in equipmentcomb:
    if len( set(comb)) != len(comb):   #Ignore when 2 rings are the same
        continue

    totaldamage = sum(equipdict[item]['damage'] for item in comb)
    totalarmor = sum(equipdict[item]['armor'] for item in comb )
    if player_win(totaldamage, totalarmor):
        minimum = min(minimum, sum(equipdict[item]['cost'] for item in comb ))
    else:
        maximum = max(maximum, sum(equipdict[item]['cost'] for item in comb ))

print(f"Least amount for victory: ${minimum}\nMaximum amount and defeat: ${maximum}")