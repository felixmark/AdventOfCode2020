"""
Advent of Code 2020 Day 01
"""

import os


def task1(numbers):
    for pos1 in range(0, len(numbers)):
        for pos2 in range(pos1, len(numbers)):
            if (2020 - numbers[pos1]) == numbers[pos2]:
                return numbers[pos1] * numbers[pos2]
    return None


def task2(numbers):
    for pos1 in range(0, len(numbers)):
        for pos2 in range(pos1 + 1, len(numbers)):
            for pos3 in range(pos2 + 1, len(numbers)):
                if (2020 - numbers[pos1] - numbers[pos2]) == numbers[pos3]:
                    return numbers[pos1] * numbers[pos2] * numbers[pos3]
    return None


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        input_string = input_file.read()
        numbers = list(map(int, input_string.splitlines(False)))
        print("Solution 1: " + str(task1(numbers)))
        print("solution 2: " + str(task2(numbers)))


if __name__ == '__main__':
    main()
