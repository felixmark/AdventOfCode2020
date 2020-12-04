"""
Advent of Code 2020 Day 04
"""

import os
import re


def parse_passport(str_passport):
    parsed_passport = {}
    for str_property in re.findall(r"(...:\S+)", str_passport, re.IGNORECASE):
        str_key = re.search(r"(...):", str_property, re.IGNORECASE).groups()[0]
        str_value = re.search(r":(\S+)", str_property, re.IGNORECASE).groups()[0]
        parsed_passport[str_key] = str_value
    return parsed_passport


def is_valid_passport(passport):
    set_fields = 0
    set_fields += int("ecl" in passport)
    set_fields += int("pid" in passport)
    set_fields += int("eyr" in passport)
    set_fields += int("hcl" in passport)
    set_fields += int("byr" in passport)
    set_fields += int("iyr" in passport)
    set_fields += int("hgt" in passport)
    return set_fields == 7


def property_check(passport):
    correct_fields = 0

    # Height
    re_height = re.search(r"(\d+)[cm|in]", passport["hgt"])
    height = None if re_height is None else int(re_height.groups()[0])
    is_cm = "cm" in passport["hgt"]

    # Eye color
    valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    correct_fields += int(1920 <= int(passport["byr"]) <= 2002)
    correct_fields += int(2010 <= int(passport["iyr"]) <= 2020)
    correct_fields += int(2020 <= int(passport["eyr"]) <= 2030)
    correct_fields += int(height is not None and ((is_cm and (150 <= height <= 193)) or (not is_cm and (59 <= height <= 76))))
    correct_fields += int(len(re.findall(r"(#([0-9]|[a-f]){6})", passport["hcl"])) == 1)
    correct_fields += int(passport["ecl"] in valid_eye_colors)
    correct_fields += int(len(re.findall(r"^(\d{9})$", passport["pid"])) == 1)
    return correct_fields == 7


def main():
    valid_passports = 0
    perfect_passports = 0
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        str_passport = ""
        while line := input_file.readline():
            if len(line) > 1:
                str_passport += line
            else:
                passport = parse_passport(str_passport)
                if is_valid_passport(passport):
                    valid_passports += 1
                    if property_check(passport):
                        perfect_passports += 1
                str_passport = ""

    print("Solution 1: " + str(valid_passports))
    print("Solution 2: " + str(perfect_passports))


if __name__ == '__main__':
    main()
