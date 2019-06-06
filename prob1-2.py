"""Problem 1, day 2:
Write and test a function that accepts a string as an argument and prints out
whether this string is a palindrome or not. (A palindrome is a string that
reads the same forwards and backwards.)


Assume non-null input.
"""


def palindrome(input: str) -> None:

    index = 0
    ispalindrome = True

    while index <= len(input)//2:
        if input[index] == input[-(index + 1)]:
            ispalindrome = True
        else:
            ispalindrome = False
            break
        index += 1

    if ispalindrome == False:
        print(f'{input} is not a palindrome.')
    else:
        print(f'{input} is a palindrome.')
