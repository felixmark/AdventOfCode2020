# Advent of Code 2020
My solutions for the [Advent of Code 2020](https://adventofcode.com/2020).

##### Table of Contents
- [Day 1](#day-1)  
- [Day 2](#day-2)  

---

## Day 1
**Task 1**  
Find two numbers in a list that add up to the value 2020.  
The solution is the product of the two values.  
  
**Task 2**  
Find three numbers in a list that add up to the value 2020.  
The solution is the product of the three values.

## Day 2
**Task 1**  
Each line of the input file gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, ```1-3 a``` means that the password must contain a at least 1 time and at most 3 times. So ```1-3 a: somepassword``` would be valid since _somepassword_ contains at least 1 _a_ and at most 3 _a_.  
The solution is the number of valid passwords from the input file.  
  
**Task 2**  
This time the numbers at the beginning represent two positions in the password for the given character. If the character occurs in exactly one of them the password is valid. If the character is at no position or at both the password is invalid. So a correct password would be `2-4 a: password` while `2-4 a: pasaword` and `2-4 a: psssword` would be incorrect.  
The solution is the number of valid passwords from the input file.
