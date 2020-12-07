"""
Advent of Code 2020 Day 07
"""

import os
import re


def parse_bag(str_line):
    bag_color = re.findall(r"(.*)bags contain", str_line, re.IGNORECASE)[0].strip()
    inner_bags_string = str_line[str_line.index("contain ")+8:].replace("bags", "").replace("bag", "").replace(".", "").replace("no other", "").strip()

    if len(inner_bags_string) > 1:
        inner_bags = [
            {
                "color": inner_bag.strip()[inner_bag.strip().index(" ")+1:],
                "amount": int(inner_bag.strip()[0:inner_bag.strip().index(" ")])
            } for inner_bag in inner_bags_string.split(", ")]
    else:
        inner_bags = []

    return {
        "color": bag_color,
        "inner_bags": inner_bags
    }


def check_bags_for_bag_recursive(bag_dictionary, search_color, bag_color):
    bag = bag_dictionary[bag_color]
    for inner_bag in bag["inner_bags"]:
        if inner_bag["color"] == search_color or check_bags_for_bag_recursive(bag_dictionary, search_color, inner_bag["color"]):
            return True
    return False


def count_bags_in_bag_recursive(bag_dictionary, search_color, count):
    bag = bag_dictionary[search_color]
    count += 1
    for inner_bag in bag["inner_bags"]:
        multiplier = inner_bag["amount"]
        count += multiplier * count_bags_in_bag_recursive(bag_dictionary, inner_bag["color"], 0)
    return count


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        bag_dictionary = {}
        str_arr_lines = input_file.read().splitlines(False)
        for str_line in str_arr_lines:
            bag_with_rule = parse_bag(str_line)
            bag_dictionary[bag_with_rule["color"]] = bag_with_rule

    count = 0
    for bag in bag_dictionary:
        if check_bags_for_bag_recursive(bag_dictionary, "shiny gold", bag):
            count += 1
    print("Solution 1: " + str(count))

    count = count_bags_in_bag_recursive(bag_dictionary, "shiny gold", 0) - 1
    print("Solution 2: " + str(count))


if __name__ == '__main__':
    main()
