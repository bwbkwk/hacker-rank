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

def isValid(s):
    cnt = Counter(s)
    freq = [cnt[k] for k in cnt]
    cnt = Counter(freq)
    
    if len(cnt) == 1:
        return "YES"
    if len(cnt) > 2:
        return "NO"
    mc = cnt.most_common(2)
    
    if mc[1][0] == 1 and mc[1][1] == 1:
        return "YES"
    if mc[0][0]+1 == mc[1][0] and mc[1][1] == 1:
        return "YES"
    return "NO"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
