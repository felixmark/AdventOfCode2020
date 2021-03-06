# Advent of Code 2020
My solutions for the [Advent of Code 2020](https://adventofcode.com/2020).
I have only done day 1 to 13 since I have been kind of busy after that.

##### Advent Calendar
[Day 01](#day-1),  [Day 02](#day-2),  [Day 03](#day-3),  [Day 04](#day-4),  [Day 05](#day-5),  
[Day 06](#day-6),  [Day 07](#day-7),  [Day 08](#day-8),  [Day 09](#day-9),  [Day 10](#day-10),  
[Day 11](#day-11), [Day 12](#day-12), [Day 13](#day-13)

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
A list of numbers has to be searched for a number, that can not be created by adding two of the previous 25 numbers up.  
The solution is the number, which can not be created.

**Task 2**  
The number from task 1 has to be created by adding up a contiguous row of numbers, consisting of 2 or more numbers.  
The solution is the sum of the smallest and largest value within the row of numbers.


## Day 10
**Task 1**  
A list of adapter "Joltages" has to be analyzed. All the adapters shall be used, and the Joltage differences between each adapter should be counted.  
The solution is the amount of 1 Jolt differences multiplied by the amount of 3 Jolt differences.

**Task 2**  
The solution for Task two is the total number of distinct ways you can arrange the adapters to connect the charging outlet to the device.  
(This task took me too long, so it is still unfinished.)


## Day 11
**Task 1**  
An array of seats and floor parts in a grid is given. Each seat can be free or taken. When people arrive, each seat without a taken seat surrounding it will be taken. A seat with 4 or more free seats around it will be freed. After a finite amount of iterations, the system stabilizes, and no more seats are taken or freed.  
The solution is the amount of seats taken at the end.

**Task 2**  
This time, not only the seats surrounding the seat should be considered, but all seats in direct line of sights (lika a queen moves on a chess board). Furthermore this time a seat is only freed when 5 or more seats in sight are taken. Again, after a finite amount of iterations, the system stabilizes, and no more seats are taken or freed.  
The solution is the amount of seats taken at the end.


## Day 12
**Task 1**  
A ferry should be navigated by a list of instructions:  
```
Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is currently facing.
```
After all the instructions are executed, the Manhattan's distance should be executed (position x + position y).  
The solution is the Manhattan's distance after all instructions are executed.

**Task 2**  
This time the list of instructions given shall be applied to a waypoint, and not the ferry itself.
The instructions are:
```
Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
Action F means to move forward to the waypoint a number of times equal to the given value.
```
The solution is the Manhattan's distance after all instructions are executed.

## Day 13
**Task 1**  
A bus departure list should be checked for the earliest bus that arrives after a certain time. 
The solution is the ID of the earliest bus multiplied by the number of minutes it will take to wait for that bus.