"""
Advent of Code 2020 Day 06
"""

import os


def cnt_correct_answers_of_group(str_answers):
    list_answers = []
    for line in str_answers.splitlines(False):
        for char in line:
            if char not in list_answers:
                list_answers.append(char)
    return len(list_answers)


def cnt_correct_answers_of_group2(str_answers):
    dict_answers = {}
    people_cnt = 0
    all_the_same_cnt = 0
    for line in str_answers.splitlines(False):
        people_cnt += 1
        for char in line:
            if char not in dict_answers:
                dict_answers[char] = 1
            else:
                dict_answers[char] += 1

    for answer in dict_answers:
        if dict_answers[answer] == people_cnt:
            all_the_same_cnt += 1
    return all_the_same_cnt


def main():
    all_any_answers_cnt = 0
    all_same_answers_cnt = 0
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        str_group_answers = ""
        while line := input_file.readline():
            if len(line) > 1:
                str_group_answers += line
            else:
                all_any_answers_cnt += cnt_correct_answers_of_group(str_group_answers)
                all_same_answers_cnt += cnt_correct_answers_of_group2(str_group_answers)
                str_group_answers = ""
        all_any_answers_cnt += cnt_correct_answers_of_group(str_group_answers)
        all_same_answers_cnt += cnt_correct_answers_of_group2(str_group_answers)

    print("Solution 1: " + str(all_any_answers_cnt))
    print("Solution 2: " + str(all_same_answers_cnt))


if __name__ == '__main__':
    main()
