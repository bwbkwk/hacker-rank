#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    unq_s = set(s.lower())
    if ' ' in unq_s:
        unq_s.remove(' ')
    alphabets = set(string.ascii_lowercase)
    
    if len(alphabets - unq_s) == 0:
        return 'pangram'
    return 'not pangram'
    
    
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
