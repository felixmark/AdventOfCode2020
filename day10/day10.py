"""
Advent of Code 2020 Day 10
"""
import os

def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        input_string = input_file.read()
        number_list = list(map(int, input_string.splitlines(False)))
        number_list.sort()
        number_list.append(number_list[len(number_list) - 1] + 3)
        print(str(number_list))

        joltage_steps = []
        previous_joltage = 0
        for joltage in number_list:
            joltage_steps.append(joltage - previous_joltage)
            previous_joltage = joltage
        print("Solution 1: " + str(joltage_steps.count(1) * joltage_steps.count(3)))
        print("="*20)

        # Part 2
        chargers = []
        position = 0
        for joltage in number_list:
            upper_boundary = min(position + 3, len(number_list) - 1)
            children = []
            child_position = position + 1

            print("Charger #" + str(position) + " value: " + str(joltage) + " children: ", end='')
            for child in number_list[position+1:upper_boundary + 1]:
                if child <= joltage + 3:
                    children.append(child_position)
                child_position += 1
            chargers.append({'joltage': joltage, 'child_positions': children})
            print(','.join([str(child) for child in children]))

            position += 1

        count = 1
        for charger in chargers:
            if len(charger['child_positions']) > 0:
                count *= len(charger['child_positions'])

        print("Solution 2: " + str(count*2))

        """
        NOT:
        1176956575385002643219210516851437453019191645837006471168 (too high)
        3770480261413891767985083711133946210897905968
        5997013881313296384
        11994027762626592768
        """

if __name__ == '__main__':
    main()
