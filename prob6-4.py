"""Prob6-day4, python version:
•	Write and test functions in both JavaScript and Python, named 'explode'
that take a string and return an array (JS) or list (Python) consisting of
the individual characters of the argument string.
"""

from typing import List

def explode(strng: str) -> List:
    answer = []
    for ch in strng:
        answer.append(ch)
    return answer
