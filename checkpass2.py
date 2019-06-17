"""
password checker: this will check with buckets the avg composition of a pass,
avg length, and see how uniformly distributed our generating function is.
"""

import secrets
import string

"""
# want to creat a dict that has character:count, key:value pairs to check
#the pass composition and keep track through each iteration.  finally output
#the avgcount/len(alpha) as a measure for how random the passes are, and
#output dict to see the result
"""

minlen = 8
maxlen = 16
length = maxlen
alpha = string.ascii_letters + string.digits + string.punctuation

def genpass() -> str:
        length = secrets.choice(range(minlen,maxlen+1))
        return ''.join(secrets.choice(alpha) for i in range(length))


def passchecker(passw):
    i = 0
    alpha = string.ascii_letters + string.digits + string.punctuation
    runs = 10000 #num of passwords we check to get our results
    totlen = 0 #save tot len to help with avg comp later
    avglen = 0 # totlen/runs at end

    #make our composition dict
    composition = {alpha[i]:0 for i in range(len(alpha))}

    while i < runs:
        password = passw()
        totlen += len(password)

        for ch in password:
            composition[ch] = composition[ch] + 1
        i += 1

    print('Avg length: ', totlen/runs, '\n', composition)
