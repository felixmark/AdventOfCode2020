"""
Advent of Code 2020 Day 03
"""

import os


def task(field, right, down):
    pos = [0, 0]
    tree_cnt = 0
    while pos[1] < len(field):
        if field[pos[1]][pos[0]] == "#":
            tree_cnt += 1
        pos[0] = (pos[0] + right) % len(field[0])
        pos[1] = pos[1] + down
    return tree_cnt


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        input_string = input_file.read()
        field = input_string.splitlines(False)
        one = task(field, 1, 1)
        two = task(field, 3, 1)
        three = task(field, 5, 1)
        four = task(field, 7, 1)
        five = task(field, 1, 2)
        print("Solution 1: " + str(two))
        print("Solution 2: " + str(one * two * three * four * five))


if __name__ == '__main__':
    main()
