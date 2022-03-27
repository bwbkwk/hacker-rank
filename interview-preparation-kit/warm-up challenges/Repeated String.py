#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    
    # count occurences of 'a' ini string s
    count = sum([1 if c == 'a' else 0 for c in s])
    
    # see how many s can fit in the length of n (rc)
    repeatCount = n // len(s)
    
    # multiply count by value of rc
    count *= repeatCount
    
    # just count the uncovered occurence of 'a'
    # in the left substring, e.g. with s='aabc' and n=6
    #  [1234(56)]78
    # '[aabc(aa)]bc'
    # count value will be 1 and the left string is 'aa' since
    # the code below count the rest of 'a' in left substring
    for c in s[:n - repeatCount * len(s)]:
        if c == 'a':
            count+=1
    return count
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
