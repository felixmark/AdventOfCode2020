"""
Advent of Code 2020 Day 05
"""

import os


def parse_seat(str_row, str_col, total_rows, total_columns):
    # Row of the plane
    guess_row = [0, total_rows - 1]
    for char in str_row:
        guess_row[0 if char == "B" else 1] = int((guess_row[0] + guess_row[1] + (0 if char == "F" else 1)) / 2)
    parsed_seat = guess_row[0] * 8

    # Column of the plane
    guess_col = [0, total_columns - 1]
    for char in str_col:
        guess_col[0 if char == "R" else 1] = int((guess_col[0] + guess_col[1] + (0 if char == "L" else 1)) / 2)
    parsed_seat += guess_col[0]
    return parsed_seat


def find_my_seat(taken_seats):
    taken_seats.sort()
    free_seats = []
    for seat in taken_seats:
        if not ((seat - 1) in taken_seats):
            if (seat - 1) in free_seats:
                return seat - 1
            free_seats.append(seat - 1)
        if not ((seat + 1) in taken_seats):
            if (seat + 1) in free_seats:
                return seat + 1
            free_seats.append(seat + 1)


def main():
    highest_seat_number = 0
    taken_seats = []
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        while line := input_file.readline().strip():
            parsed_seat_number = parse_seat(line[0:7], line[7:10], 128, 8)
            taken_seats.append(parsed_seat_number)
            if highest_seat_number < parsed_seat_number:
                highest_seat_number = parsed_seat_number

    print("Solution 1: " + str(highest_seat_number))
    print("Solution 2: " + str(find_my_seat(taken_seats)))


if __name__ == '__main__':
    main()
