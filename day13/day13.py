"""
Advent of Code 2020 Day 13
"""

import os
from math import sqrt, prod


def parse_busses(str_line):
    busses = str_line.split(',')
    busses = [int(bus_interval) for bus_interval in list(filter('x'.__ne__, busses))]
    return busses


all_primes = None


def merge_primes(primes):
    global all_primes
    if all_primes is None:
        all_primes = primes
    else:
        for prime in primes:
            if all_primes.count(prime) < primes.count(prime):
                all_primes.append(prime)


def find_primes(num):
    primes = []
    while num % 2 == 0:
        primes.append(2)
        num /= 2

    for i in range(3, int(sqrt(num)+2)):
        while num % i == 0:
            primes.append(i)
            num /= i
        i += 2

    if num > 2:
        primes.append(num)

    print("Num: " + str(num) + " parts: " + str(primes))
    merge_primes(primes)
    print("All primes: " + str(all_primes))


def main():
    with open(os.path.dirname(os.path.realpath(__file__)) + os.path.sep + "input.txt", "r") as input_file:
        input_string = input_file.read()
        lines = input_string.splitlines(False)
        time_now = int(lines[0])
        print("Time now: " + str(time_now))
        bus_intervals = parse_busses(lines[1])

        # PART 1
        shortest_waiting_time = None
        bus_id = None
        for bus_interval in bus_intervals:
            print("Checking Bus: " + str(bus_interval))
            if shortest_waiting_time is None or (bus_interval - time_now % bus_interval) < shortest_waiting_time:
                shortest_waiting_time = bus_interval - time_now % bus_interval
                print("Found Bus: " + str(bus_interval) + " with a waiting time of " + str(shortest_waiting_time) + ".")
                bus_id = bus_interval
        print("Solution 1: " + str(bus_id * shortest_waiting_time))

        # PART 2
        for bus_interval in bus_intervals:
            find_primes(bus_interval)
        timepoint_where_all_times_are_0 = prod(all_primes)
        shortest_time = min(bus_intervals)
        print("Shortest bus_time: " + str(shortest_time))

        print("Solution 2: " + str(timepoint_where_all_times_are_0 - shortest_time))   # NOT 1463175673841141, 1463175673841128


if __name__ == '__main__':
    main()
