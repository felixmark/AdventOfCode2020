"""
Advent of Code 2020 Day 09
"""

import os


def is_valid_number(number_list, pos_from, pos_to, checked_value):
    for pos1 in range(pos_from, pos_to+1):
        for pos2 in range(pos1, pos_to+1):
            if (checked_value - number_list[pos1]) == number_list[pos2]:
                return False
    return True


def find_contiguous_set(number_list, pos_from, invalid_number):
    for pos_to in range(pos_from + 1, len(number_list) - 1):
        if sum(number_list[pos_from:pos_to]) == invalid_number:
            sublist = number_list[pos_from:pos_to]
            return min(sublist) + max(sublist)
    return None


def main():
    preamle = 25
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        input_string = input_file.read()
        number_list = list(map(int, input_string.splitlines(False)))

        pos_from = 0
        invalid_number = 0
        for checked_value_index in range(preamle, len(number_list) - 1):
            checked_value = number_list[checked_value_index]
            pos_to = checked_value_index - 1
            if is_valid_number(number_list, pos_from, pos_to, checked_value):
                invalid_number = checked_value
            pos_from += 1
        print("Solution 1: " + str(invalid_number))

        solution2 = 0
        for pos_from in range(0, len(number_list) - 1):
            solution2 = find_contiguous_set(number_list, pos_from, invalid_number);
            if solution2 is not None:
                break;
        print("Solution 2: " + str(solution2))


if __name__ == '__main__':
    main()
