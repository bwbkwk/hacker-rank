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
    s = s[:n]
    count = sum([1 if c == 'a' else 0 for c in s])
    repeatCount = math.floor(n / len(s))
    count *= repeatCount
    
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
