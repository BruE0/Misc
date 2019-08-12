#!/usr/bin/env python3
# periodic_table.py
# 2019.06

import csv


def load_csv(path):
    periodic_table = {}
    with open(path, "r") as f:
        reader = csv.reader(f)

        keys = next(reader)

        keys = [x.strip() for x in keys]

        for element_data in reader:
            periodic_table[element_data[1].strip()] = dict(
                zip(keys, (v.strip() for v in element_data)))
    return keys, periodic_table


def symbol_inputloop(dictionary):
    while True:
        symbol = input("\nEnter element symbol: >")
        if symbol in dictionary:
            return symbol
        else:
            print("Wrong symbol.")


def input_choice(keys):
    print("\nChoose a number: \n")
    print('\n'.join([f"{i}: {k}" for i, k in enumerate(keys)]))
    choice = input("> ")
    if choice.isdigit() and (int(choice) in range(len(keys))):
        return int(choice)
    else:
        return -1

def main():
    keys, table = load_csv("periodic_table.csv")
    
    while True:
        print(', '.join(table))
        symbol = symbol_inputloop(table)
        choice = input_choice(keys)
        if choice != -1:
            key = keys[choice]
            print(f">>[{table[symbol]['Symbol']}] "
                  f"{table[symbol]['Name']}: \"{key}\" = ",
                     table[symbol][key], "\n")


if __name__ == "__main__":
    main()
