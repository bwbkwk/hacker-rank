#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# soon to be commented
def isValid(s):
    cs = Counter(s)
    freq = Counter([cs[k] for k in cs])
    
    # print(freq)
    most_common = freq.most_common(3)
    print(most_common)
    if len(most_common) > 2:
        return "NO"
    if len(most_common) == 1:
        return "YES"
    if most_common[1] == (1,1):
        return "YES"
    
    return "YES" if abs(most_common[1][0] - most_common[0][0]) ==1 and most_common[1][1] == 1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
