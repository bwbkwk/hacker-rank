#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    dHelper = Counter()
    # just count the occurences of every sock
    for x in ar:
        dHelper[x] += 1
        
    pairs = 0
    
    for x in dHelper:
        # sock that has no pair will not contribute to pairs variable
        # since x.5 => x by operator '//'
        pairs += dHelper[x] // 2
    return int(pairs)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
