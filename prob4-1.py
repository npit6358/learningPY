"""Prob1 day 4:

1. Define and test a function in Python that takes a list as input and makes a
new list that has all the elements that are odd numbers from this list in it
and prints out this new list.
"""

#from typing import List

"""straight forward way
def ret_odds(lst: List) -> None:

    odds = []

    for el in lst:
        if el % 2 != 0:
            odds.append(el)

    print(odds)
"""

"""
#using different methods and functions for practice.  not a good method.
import random
from typing import List

def ret_odds(lst: List) -> None:

    num_odds = 0
    new_lst = lst

    #find number of odds in the list for later splicing.
    for el in new_lst:
        if el % 2 != 0:
            num_odds += 1

    #sort list based on evenness so we can splice out the odds and print.
    new_lst.sort(key=lambda x: x % 2 != 0)
    #print odds by splicing the list, from right (as True comes first and
    #odd is assigned a False value.
    print(new_lst[-num_odds:])
"""

import random
from typing import List

#this is the easiest way with the filter function.
def ret_odds(lst: List):
    print(list(filter(lambda item: (item % 2 != 0), lst)))


#make rand 100 int list for testing.
rnd_list = []
while input('Enter for random list or (q)uit? ') != 'q':
    rnd_list = [random.randint(0,100) for el in range(100)]

    print("our random list is: ")
    print(rnd_list)

    print("odd list is: ")
    ret_odds(rnd_list)

    rnd_list =[]
