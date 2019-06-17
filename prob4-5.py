"""Prob4-day5:
Define and test a function in Python, that inverts a dictionary. It should
accept a dictionary as a parameter and return a dictionary where the keys
are values from the input dictionary and the values are lists of keys from
the input dictionary.
Input: { "key1" : "value1", "key2" : "value2", "key3" : "value1" }
Return: { "value1" : ["key1", "key3"], "value2" : ["key2"] }
"""


"""this gives right answer to above input-return prompt, but it isn't an actual
inverse function as we can't inverse the inverse to get our original input.
we get a typerror unhashable type: 'list'.  maybe if turn into a tuple at some
point then back to a list it'll work as a tuple is hashable.
"""

def inverse(dic):
    dic = {"key1" : "value1", "key2" : "value2", "key3" : "value1"}
    newdic = {}

    for key, value in dic.items():
        if value in newdic.keys():
            newdic[value].append(key)
        else:
            newdic[value] = [key]

    print(newdic)
