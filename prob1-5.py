"""Prob1-day5:
Define and test functions in both JavaScript and Python, that accept a
dictionary and a value, and return how many times that value occurs in
the dictionary.
"""

def valuecount(dicts: dict, value) -> int:
    count = 0
    for val in list(dicts.values()):
        if val == value:
            count += 1

    return count
