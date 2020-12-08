# Advent of Code 2020
My solutions for the [Advent of Code 2020](https://adventofcode.com/2020).

##### Advent Calendar
[Day 01](#day-1),  [Day 02](#day-2),  [Day 03](#day-3),  [Day 04](#day-4),  [Day 05](#day-5),  
[Day 06](#day-6),  [Day 07](#day-7),  [Day 08](#day-8),  [Day 09](#day-9),  [Day 10](#day-10),  
[Day 11](#day-11), [Day 12](#day-12), [Day 13](#day-13), [Day 14](#day-14), [Day 15](#day-15),  
[Day 16](#day-16), [Day 17](#day-17), [Day 18](#day-18), [Day 19](#day-19), [Day 20](#day-20),  
[Day 21](#day-21), [Day 22](#day-22), [Day 23](#day-23), [Day 24](#day-24), [Day 25](#day-25)  

---

## Day 1
**Task 1**  
Find two numbers in the input file that add up to the value 2020.  
The solution is the product of the two values.  
  
**Task 2**  
Find three numbers in the input file that add up to the value 2020.  
The solution is the product of the three values.


## Day 2
**Task 1**  
Each line of the input file gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, `1-3 a` means that the password must contain a at least 1 time and at most 3 times. So `1-3 a: somepassword` would be valid since `somepassword` contains at least 1 `a` and at most 3 `a`.  
The solution is the number of valid passwords from the input file.  
  
**Task 2**  
This time the numbers at the beginning represent two positions in the password for the given character. If the character occurs in exactly one of them the password is valid. If the character is at no position or at both the password is invalid. So a correct password would be `2-4 a: password` while `2-4 a: pasaword` and `2-4 a: psssword` would be incorrect.  
The solution is the number of valid passwords from the input file.


## Day 3
**Task 1**  
The input file contains a map. The map shows locations of trees represented by a `#`. You begin at the top left of the map and try to get to the very bottom. When the map ends horizontally, it is considered to be tiled, so you begin again from the left.  
The solution is the amount of trees you encounter when moving 3 steps to the right and 1 to the bottom each step.

**Task 2**  
This time the steps change, and you have to calculate different patterns. For instance 1 step to the right and 1 step down and others.  
The solution is the product of the amount of trees encountered with each pattern given.


## Day 4
**Task 1**  
The input file contains passports separated by empty lines. The passports have to have 7 properties without checking the actual content of them.  
The solution is the amount of valid passports within the input file.

**Task 2**  
For task two the properties of the passports (id, height, eye color, etc.) have to be in given boundaries, to be valid.  
The solution is the new amount of valid passports.


## Day 5
**Task 1**  
A string representing a seat ID in a plane has to be parsed into an actual ID of it. The input looks like this: `FBBFFFBRRL` where F means Front, B means Back, L means Left and R means Right. There are 128 rows and 8 columns. F and L means "keep the lower half", where B and R means "keep the upper half". By applying this rule to all the seats a seat ID can be created by calculating it with: `row * 8 + col`.  
The solution is the ID of the last seat with the highest ID.

**Task 2**  
Now the one empty seat in the plane, which is not at the front or at the end has to be found.  
The solution is the ID of the free seat in the plane.

## Day 6
**Task 1**  
A list of answers from groups of people should be analyzed for any answer anybody has ticked as "yes".  
The solution is the sum of all ticked answers per group. So if group 1 ticked 3 answers and group 2 ticked 2 answers as yes the solution is 5. 

**Task 2**  
This time only answers which everybody from each group answered with "yes" should be counted.  
The solution is the sum of all ticked answers per group where everyone of the group answered with "yes".


## Day 7
**Task 1**  
A set of rules for bags containing other bags are given. For instance a red bag contains 4 blue bags and 2 green bags. A blue bag contains 3 yellow bags.  
The solution is how many bags may contain your shiny gold bag.

**Task 2**  
The solution for task 2 is the amount of other bags in your shiny gold bag.  


## Day 8
**Task 1**  
A list of instructions and values has to be executed. The instructions are `acc <value>` (global variable + value), `jmp <value>` (jump to command <value> steps from this command) and `nop <value>` (do nothing). The lines of instructions contain an endless loop.  
The solution is the value of the global variable when the first instruction is executed twice.

**Task 2**  
One of the `jmp` instructions has to be replaced with a `nop` instruction, or a `nop` instruction has to be replaced with a `jmp` instruction, so that the program can finish without an endless loop.  
The solution is the value of the global variable after the program finishes execution correctly.


## Day 9
**Task 1**  
???  

**Task 2**  
???  


## Day 10
**Task 1**  
???  

**Task 2**  
???  


## Day 11
**Task 1**  
???  

**Task 2**  
???  


## Day 12
**Task 1**  
???  

**Task 2**  
???  


## Day 13
**Task 1**  
???  

**Task 2**  
???  


## Day 14
**Task 1**  
???  

**Task 2**  
???  


## Day 15
**Task 1**  
???  

**Task 2**  
???  


## Day 16
**Task 1**  
???  

**Task 2**  
???  


## Day 17
**Task 1**  
???  

**Task 2**  
???  


## Day 18
**Task 1**  
???  

**Task 2**  
???  


## Day 19
**Task 1**  
???  

**Task 2**  
???  


## Day 20
**Task 1**  
???  

**Task 2**  
???  


## Day 21
**Task 1**  
???  

**Task 2**  
???  


## Day 22
**Task 1**  
???  

**Task 2**  
???  


## Day 23
**Task 1**  
???  

**Task 2**  
???  


## Day 24
**Task 1**  
???  

**Task 2**  
???  


## Day 25
**Task 1**  
???  

**Task 2**  
???  
