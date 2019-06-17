"""Prob9-day4:
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of 8 or more lowercase letters,
uppercase letters, digits, and symbols ( _   ,   or  -). The passwords should
be random, their lengths should be random (between 8 and 16) generating a new
password every time the user asks for a new one. Include your run-time code
in a main method.
"""

import secrets
import string

length = 16
alpha = string.ascii_letters + string.digits + string.punctuation


def main():
    while input("Enter for new password or (q)uit?") != 'q':
        length = secrets.choice(range(8,17))
        print(''.join(secrets.choice(alpha) for i in range(length+1)))

main()
