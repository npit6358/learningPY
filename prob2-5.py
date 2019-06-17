"""Prob2-day5:
Define and test functions in both JavaScript and Python, that accept a
dictionary and a value, and return the number of times that value is used
as a key in the dictionary.
"""

def keycount(dicts: dict, value) -> int:
    count = 0
    for val in list(dicts.keys()):
        if val == value:
            count += 1

    return count
