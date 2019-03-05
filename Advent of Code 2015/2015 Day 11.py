# Advent of Code 2015. Day 11#
#
#


def increment(string):
    oldlen = len(string)
    string = string.rstrip('z')
    string = string[:-1] + chr(ord(string[-1]) + 1) + "a" * (oldlen - len(string))
    return string


def increasing(string):
    chars = list(string)
    for index in range(len(chars)-2):
        if ord(chars[index + 2]) == ord(chars[index + 1]) + 1 == ord(chars[index]) + 2:
            return True
    return False


def pairs(string):
    charset = set(string)
    count = sum(map(string.count, [char * 2 for char in charset]))
    return count >= 2


password = "hxbxwxba"

for _ in range(969412):
    password = increment(password)
    if ("i" in password) or ("o" in password) or ("l" in password):
        continue
    if increasing(password) and pairs(password):
        print(f"Next password: {password}")
