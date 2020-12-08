"""
Advent of Code 2020 Day 08
"""

import os
import copy


def parse_instruction(str_line):
    str_line = str_line.replace('+', '')
    return {
        'instruction': str_line[:3],
        'value': int(str_line[4:]),
        'times_executed': 0
    }


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input.txt', 'r') as input_file:
        instruction_dictionary = {}
        line_num = 0
        str_arr_lines = input_file.read().splitlines(False)
        for str_line in str_arr_lines:
            instruction_dictionary[line_num] = parse_instruction(str_line)
            line_num += 1


    # Part 1
    next_instruction = 0
    global_variable = 0
    part1_dictionary = copy.deepcopy(instruction_dictionary)
    while True:
        instruction = part1_dictionary[next_instruction]
        print(str(next_instruction) + " - " + instruction['instruction'] + ": " + str(instruction['value']))
        if instruction['times_executed'] > 0:
            break

        if instruction['instruction'] == 'acc':
            global_variable += instruction['value']
            instruction['times_executed'] += 1
            next_instruction += 1
        elif instruction['instruction'] == 'jmp':
            instruction['times_executed'] += 1
            next_instruction += instruction['value']
        elif instruction['instruction'] == 'nop':
            next_instruction += 1

    print("Solution 1: " + str(global_variable))

    # Part 2
    passed_successfully = False
    change_instruction_number = 0
    while not passed_successfully:
        next_instruction = 0
        global_variable = 0
        part2_dictionary = copy.deepcopy(instruction_dictionary)

        # Modify copied dictionary
        while True:
            if change_instruction_number >= len(part2_dictionary):
                break
            instruction = part2_dictionary[change_instruction_number]
            change_instruction_number += 1
            if instruction['instruction'] == 'jmp':
                instruction['instruction'] = 'nop'
                break
            if instruction['instruction'] == 'nop':
                instruction['instruction'] = 'jmp'
                break

        # Check if this copy terminated correctly
        while True:
            if next_instruction >= len(part2_dictionary):
                passed_successfully = True
                break
            instruction = part2_dictionary[next_instruction]
            print(str(next_instruction) + " - " + instruction['instruction'] + ": " + str(instruction['value']))
            if instruction['times_executed'] > 0:
                passed_successfully = False
                break

            if instruction['instruction'] == 'acc':
                global_variable += instruction['value']
                instruction['times_executed'] += 1
                next_instruction += 1
            elif instruction['instruction'] == 'jmp':
                instruction['times_executed'] += 1
                next_instruction += instruction['value']
            elif instruction['instruction'] == 'nop':
                next_instruction += 1

    print("Solution 2: " + str(global_variable))


if __name__ == '__main__':
    main()
