"""
Advent of Code 2020 Day 02
"""

import re
import os


def task1(passwords_with_rules):
    correct_password_cnt = 0
    for pw_with_rule in passwords_with_rules:
        count = pw_with_rule["password"].count(pw_with_rule["character"])
        if pw_with_rule["from"] <= count <= pw_with_rule["to"]:
            correct_password_cnt += 1
    return correct_password_cnt


def task2(passwords_with_rules):
    correct_password_cnt = 0
    for pw_with_rule in passwords_with_rules:
        pw = pw_with_rule["password"]
        if len(pw) < pw_with_rule["from"] or len(pw) < pw_with_rule["to"]:
            continue
        first = int(pw[pw_with_rule["from"] - 1] == pw_with_rule["character"])
        second = int(pw[pw_with_rule["to"] - 1] == pw_with_rule["character"])
        if first + second == 1:
            correct_password_cnt += 1
    return correct_password_cnt


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        input_string = input_file.read()
        lines = input_string.splitlines(False)
        passwords_with_rules = []
        for line in lines:
            regex = r"(\d+)-(\d+) (.): (.+)"
            groups = re.match(regex, line, re.IGNORECASE).groups()
            passwords_with_rules.append({
                "from": int(groups[0]),
                "to": int(groups[1]),
                "character": groups[2],
                "password": groups[3]
            })
        print("Solution 1: " + str(task1(passwords_with_rules)))
        print("Solution 2: " + str(task2(passwords_with_rules)))


if __name__ == '__main__':
    main()
