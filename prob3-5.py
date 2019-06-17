"""Prob3-day5:
Define and test functions in both JavaScript and Python, that accept a
dictionary and a value, and return a list of the keys which are paired
with that value in the dictionary.
"""

def keywithvalue(dicts: dict, value) -> list:
    out = []
    count = 0
    for key in dicts:
        if dicts[key] == value:
            out.append(key)

    return out
