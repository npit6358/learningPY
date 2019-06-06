"""Problem 10:
Write and test a function that accepts a positive number as the parameter and
determines if the number is a “Perfect Number”. A Perfect Number is one whose
divisors sum to the number itself.
Ex:    28 = 1 + 2 + 4 + 7 + 14

Brute force again.
"""


def isperfect(number: int) -> str:

    summ = 1                #1 is divisor to every number

    #test for divisors
    divisor = 2
    while divisor <= number/2.0:

        if number % divisor == 0: summ += divisor
        
        divisor += 1

    #test if perfect
    if summ == number:
        print(f'{number} is a perfect number.')
    else:
        print(f'{number} is not a perfect number.')
