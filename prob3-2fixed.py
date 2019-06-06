"""prob3 day 2:
Write and test a function that accepts a string argument. This will be a long
string containing multiple words. Print the string but with the words
(not the characters) reversed. For example, the string “My name is jim” would
be printed back as “jim is name my”  (not as “mij si eman yM”)

The idea is to reverse the entire string and then reverse each substring.
This gets the word order right while reversing the substring gets the word
orientation right.

Assume the spaces befoe between and after words are intended, if the whitespace
is not wanted then strip the reverse string when printing.

wordreverse('one two three four')
>>>>'four three two one'
"""

def wordreverse(string: str) -> str:

    index = 0
    stringrev = string[::-1]   #reverse our entire input string
    reverse = ""

    while index < len(string):  #while inside string
        tmplist = []

        #while not outside string index range. resolves errors from index being
        #outside permissible range as short circuit evaluation of the and leaves
        #right conjunct unevaluated.
        while index != len(string) and stringrev[index] != ' ':
                tmplist.append(stringrev[index])
                index += 1

        tmplist.reverse()  #turn most recent word around

        for i in tmplist:  #place mrw into our reversed phrase char by char.
            reverse = reverse + i
        reverse = reverse + ' '  #include space after every found word
        index += 1               #move us past most recent space

    print(reverse)
