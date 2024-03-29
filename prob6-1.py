"""Problem 6:
Write and test a function that returns the sum of multiples of
3 and 5 between 0 and limit (parameter). For example, if limit is 20,
it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
"""


def mults(limit: int) -> int:

    n  = 1
    sum = 0
    while n*3 <= limit:
        if n*3 % 15 != 0:  #Skip multiples of 15 for the n*3 case
            sum += n*3
        n += 1

    n = 1
    while n*5 <= limit:
        sum += n*5
        n += 1

    return sum
