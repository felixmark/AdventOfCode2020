"""
Advent of Code 2020 Day 02
"""

import re


def task1(pw_with_rules):
    correct_password_cnt = 0
    for pw_with_rule in pw_with_rules:
        count = pw_with_rule["password"].count(pw_with_rule["character"])
        if pw_with_rule["from"] <= count <= pw_with_rule["to"]:
            correct_password_cnt += 1
    return correct_password_cnt


def task2(pw_with_rules):
    correct_password_cnt = 0
    for pw_with_rule in pw_with_rules:
        password = pw_with_rule["password"]
        first = int(len(password) >= (pw_with_rule["from"]) and password[pw_with_rule["from"] - 1] ==
                    pw_with_rule["character"])
        second = int(len(password) >= (pw_with_rule["to"]) and password[pw_with_rule["to"] - 1] ==
                     pw_with_rule["character"])
        if first + second == 1:
            correct_password_cnt += 1
    return correct_password_cnt


def main():
    with open("input.txt", "r") as input_file:
        input_string = input_file.read()
        lines = input_string.splitlines(False)
        pw_with_rules = []
        for line in lines:
            regex = r"(\d+)-(\d+) (.): (.+)"
            groups = re.match(regex, line, re.IGNORECASE).groups()
            pw_with_rules.append({
                "from": int(groups[0]),
                "to": int(groups[1]),
                "character": groups[2],
                "password": groups[3]
            })
        print("Solution 1: " + str(task1(pw_with_rules)))
        print("Solution 2: " + str(task2(pw_with_rules)))


if __name__ == '__main__':
    main()
