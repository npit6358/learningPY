"""Prob7-day4, Python version:
	•	Write and test functions in both JavaScript and Python that take a
  string and return a string consisting of the characters of the argument
  string, each character advanced by 3 letters in the English alphabet.
"""
import string

lalpha = string.ascii_lowercase
ualpha = string.ascii_uppercase

def charAdvance(input: str) -> str:
    advance = 3
    output = ''

# tried the .islower and .isupper checks, but they caused problems with the
#.index check
    for ch in input:
        if not ch.isalpha():
            output += ch
        elif ch in lalpha:
            output += lalpha[(lalpha.index(ch) + advance) % 26]
        elif ch in ualpha:
            output += ualpha[(ualpha.index(ch) + advance) % 26]



    return output
