"""
Advent of Code 2020 Day 02
"""

def task1(passwords_with_rules):
    correct_password_cnt = 0
    for password_with_rule in passwords_with_rules:
        count = password_with_rule["password"].count(password_with_rule["character"])
        if password_with_rule["from"] <= count and count <= password_with_rule["to"]:
            correct_password_cnt += 1
    return correct_password_cnt

def task2(passwords_with_rules):
    correct_password_cnt = 0
    for password_with_rule in passwords_with_rules:
        password = password_with_rule["password"]
        first = int(len(password) >= (password_with_rule["from"]) and password[password_with_rule["from"] - 1] == password_with_rule["character"])
        second = int(len(password) >= (password_with_rule["to"]) and password[password_with_rule["to"] - 1] == password_with_rule["character"])
        if first + second == 1:
            correct_password_cnt += 1
    return correct_password_cnt
    
with open("input.txt", "r") as input_file:
    input_string = input_file.read()
    lines = input_string.splitlines(False)
    passwords_with_rules = []
    for line in lines:
        parts = line.replace(":", "").split(" ")
        values = list(map(int, parts[0].split("-")))
        passwords_with_rules.append({
            "from":         values[0],
            "to":           values[1],
            "character":    parts[1],
            "password":     parts[2]
        })
    print("Solution 1: " + str(task1(passwords_with_rules)))
    print("Solution 2: " + str(task2(passwords_with_rules)))
