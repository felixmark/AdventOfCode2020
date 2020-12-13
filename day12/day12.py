"""
Advent of Code 2020 Day 12
"""

import os


class Ferry:
    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.rot = 0
        self.waypoint_x = 10
        self.waypoint_y = -1

    def rotate(self, angle):
        self.rot += angle
        sign = 1 if self.rot >= 0 else -1
        self.rot = sign * (abs(self.rot) % 360)

    def rotate_waypoint(self, angle):
        previous_x = self.waypoint_x
        previous_y = self.waypoint_y
        if angle == 90 or angle == -270:
            self.waypoint_x = -previous_y
            self.waypoint_y = previous_x
        if angle == 180 or angle == -180:
            self.waypoint_x = -previous_x
            self.waypoint_y = -previous_y
        if angle == 270 or angle == -90:
            self.waypoint_x = previous_y
            self.waypoint_y = -previous_x

    def forward(self, value):
        if self.rot == 0:
            self.pos_x += value
        elif self.rot == -90 or self.rot == 270:
            self.pos_y -= value
        elif self.rot == 90 or self.rot == -270:
            self.pos_y += value
        elif self.rot == 180 or self.rot == -180:
            self.pos_x -= value

    def forward_to_waypoint(self, value):
        self.pos_x += value * self.waypoint_x
        self.pos_y += value * self.waypoint_y

    def calculate_manhattan_distance(self):
        return abs(self.pos_x) + abs(self.pos_y)

    def print(self):
        print("Ferry at: " + str(self.pos_x) + " " + str(self.pos_y) + " and rot: " + str(self.rot) + "°")


def parse_instruction(str_instruction):
    command = str_instruction[0]
    value = int(str_instruction[1:])
    return {'command': command, 'value': value}


def execute_instruction(ferry, instruction):
    if instruction['command'] == 'N':
        ferry.pos_y -= instruction['value']
    if instruction['command'] == 'S':
        ferry.pos_y += instruction['value']
    if instruction['command'] == 'E':
        ferry.pos_x += instruction['value']
    if instruction['command'] == 'W':
        ferry.pos_x -= instruction['value']
    if instruction['command'] == 'L':
        ferry.rotate(-instruction['value'])
    if instruction['command'] == 'R':
        ferry.rotate(instruction['value'])
    if instruction['command'] == 'F':
        ferry.forward(instruction['value'])


def execute_instruction2(ferry, instruction):
    if instruction['command'] == 'N':
        ferry.waypoint_y -= instruction['value']
    if instruction['command'] == 'S':
        ferry.waypoint_y += instruction['value']
    if instruction['command'] == 'E':
        ferry.waypoint_x += instruction['value']
    if instruction['command'] == 'W':
        ferry.waypoint_x -= instruction['value']
    if instruction['command'] == 'L':
        ferry.rotate_waypoint(-instruction['value'])
    if instruction['command'] == 'R':
        ferry.rotate_waypoint(instruction['value'])
    if instruction['command'] == 'F':
        ferry.forward_to_waypoint(instruction['value'])


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        input_string = input_file.read()
        instructions = [parse_instruction(line) for line in input_string.splitlines(False)]

        # PART 1
        ferry = Ferry()
        for instruction in instructions:
            execute_instruction(ferry, instruction)
        print("Solution 1: " + str(ferry.calculate_manhattan_distance()))

        # PART 2
        ferry2 = Ferry()
        for instruction in instructions:
            execute_instruction2(ferry2, instruction)
        print("Solution 2: " + str(ferry2.calculate_manhattan_distance()))


if __name__ == '__main__':
    main()
