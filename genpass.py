"""
password generator: set min and max length, and alpha we make choices from.
completely random no guarantee that password won't have repeats or entirely
composed of letters, digits, or punctuation by chance.
"""

import secrets
import string

minlen = 8
maxlength = 16
length = maxlength
alpha = string.ascii_letters + string.digits + string.punctuation

def genpass() -> str:
        length = secrets.choice(range(minlen,maxlen+1))
        return ''.join(secrets.choice(alpha) for i in range(length))
