"""problem 5:
    Write and test a function called oddEven that takes a parameter called limit. 
    It should print all the numbers between 0 and limit with a label to identify the even and odd numbers.
    For example, if the limit is 3, it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD

"""


def oddEven(limit: int) -> str:

    n  = 0
    while n <= limit:
        evenness = 'EVEN'
        if n % 2 != 0:
            evenness = 'ODD'
        print(str(n) + "  " + evenness)
        n += 1
    return print("\nwe're finally finished")
