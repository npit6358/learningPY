"""Problem 8:
Write and test a function that prints all the prime numbers between 0 and limit 
where limit is a parameter to the function.

Assume argument passed is > 2.

This is the brute force way with some of the basic commands and ideas.  Also
pretty slow.

curnum - the current number whose 'primeness' is under consideration.
curfact - the current possible factor we are using to do prime check.
"""



def primes(limit: int):

    print('1')              #'1' is the first prime for any limit integer.

    curnum = 3
    while curnum < limit:   #figure out if curnum is prime, print out if so.
        isprime = True      #need to init inside loop before next while loop.


        curfact=2           #curfact is the current possible factor we check.
        while curfact < curnum:
            if curnum % curfact == 0: isprime = False
            curfact += 1

        if isprime == True:
            print(curnum)

        curnum += 2         #increment curnum and start next iteration. note
                            #we halve the iterations by ignoring even numbers
                            #via our choice of increment value.
