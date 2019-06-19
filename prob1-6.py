"""prb1-day6:
Define and test a Python program that will read a large text file and will
output, in alphabetic order, a frequency distribution of the letters in the
file. You must use a text file larger than 1000 words.
"""

"""I'm gonna search for all characters, if you want to exclude some, go ahead.
"""

import string

def main():

    with open(input("give directory from root: "), "r") as infile:
        text = infile.read()

#these two lines work, but exlude search to just the english alphabet
#    alpha = string.ascii_lowercase + string.ascii_uppercase
#    alphadict = {letter:0 for letter in alpha}

    alphadict = {}
    for letters in text:
        if letters in alphadict:
            alphadict[letters] += 1
        else:
            alphadict[letters] = 1

    print(alphadict)


main()

while input('hit q to quit, else enter to start again: ') != 'q':
    main()
