"""
Advent of Code 2020 Day 11
"""

import copy
import os


def check_dir(seat_array, row_id, seat_id, offset_x, offset_y, distance=-1):
    seat_id += offset_x
    row_id += offset_y
    my_distance = 0
    while 0 <= row_id < len(seat_array) and 0 <= seat_id < len(seat_array[row_id]) and (distance < 0 or my_distance < distance):
        my_distance += 1

        if seat_array[row_id][seat_id] == 'L':
            return 0
        if seat_array[row_id][seat_id] == '#':
            return 1

        seat_id += offset_x
        row_id += offset_y
    return 0


def count_adjacent_seats(seat_array, row_id, seat_id, distance=-1):
    taken_seats = 0
    taken_seats += check_dir(seat_array, row_id, seat_id, 0, -1, distance)    # N
    taken_seats += check_dir(seat_array, row_id, seat_id, 1, -1, distance)    # NE
    taken_seats += check_dir(seat_array, row_id, seat_id, 1, 0, distance)     # E
    taken_seats += check_dir(seat_array, row_id, seat_id, 1, 1, distance)     # SE
    taken_seats += check_dir(seat_array, row_id, seat_id, 0, 1, distance)     # S
    taken_seats += check_dir(seat_array, row_id, seat_id, -1, 1, distance)    # SW
    taken_seats += check_dir(seat_array, row_id, seat_id, -1, 0, distance)    # W
    taken_seats += check_dir(seat_array, row_id, seat_id, -1, -1, distance)   # NW
    return taken_seats


def count_occupied_seats(seat_array):
    occupied_seats = 0
    for row in seat_array:
        for seat in row:
            if seat == '#':
                occupied_seats += 1
    return occupied_seats


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        input_string = input_file.read()
        original_seat_array = list([list(line) for line in input_string.splitlines(False)])
        seat_array = copy.deepcopy(original_seat_array)

        # PART 1
        stabilized = False
        while not stabilized:
            stabilized = True
            seat_array_cpy = copy.deepcopy(seat_array)
            for row_id in range(0, len(seat_array)):
                for seat_id in range(0, len(seat_array[row_id])):
                    if seat_array[row_id][seat_id] == 'L':
                        if count_adjacent_seats(seat_array, row_id, seat_id, 1) == 0:
                            seat_array_cpy[row_id][seat_id] = '#'
                            stabilized = False
                    elif seat_array[row_id][seat_id] == '#':
                        if count_adjacent_seats(seat_array, row_id, seat_id, 1) >= 4:
                            seat_array_cpy[row_id][seat_id] = 'L'
                            stabilized = False

            seat_array = copy.deepcopy(seat_array_cpy)
        print("Solution 1: " + str(count_occupied_seats(seat_array)))

        # PART 2
        seat_array = original_seat_array
        stabilized = False
        while not stabilized:
            stabilized = True
            seat_array_cpy = copy.deepcopy(seat_array)
            for row_id in range(0, len(seat_array)):
                for seat_id in range(0, len(seat_array[row_id])):
                    if seat_array[row_id][seat_id] == 'L':
                        if count_adjacent_seats(seat_array, row_id, seat_id) == 0:
                            seat_array_cpy[row_id][seat_id] = '#'
                            stabilized = False
                    elif seat_array[row_id][seat_id] == '#':
                        if count_adjacent_seats(seat_array, row_id, seat_id) >= 5:
                            seat_array_cpy[row_id][seat_id] = 'L'
                            stabilized = False
            seat_array = copy.deepcopy(seat_array_cpy)
        print("Solution 2: " + str(count_occupied_seats(seat_array)))


if __name__ == '__main__':
    main()
