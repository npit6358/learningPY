"""Prob8 day 2:
Write and test a function that accepts a numeric argument , a limit, and finds
all numbers between 1 and the limit where each digit of the number is an even
number. The numbers obtained should be printed. Ex: 76 doesn’t pass the test
(7 isn’t even) while 48 does pass and would be printed.
"""


def digitseven(limit: int) -> None:

    digits = []

    for cur_n in range(limit):
        digits = [int(digit) for digit in str(cur_n)]

        if all(list(map(lambda digit: digit % 2 == 0, digits))):
            print(cur_n)

        digits =[]
