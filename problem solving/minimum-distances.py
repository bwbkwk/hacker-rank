#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    ls = [(x,i) for i,x in enumerate(a)]
    
    ls = sorted(ls)
    d = dict()
    min_dist = 100000
    for k,v in ls:
        if k in d:
            min_dist = min(v - d[k],min_dist)
        d[k] = v
    if 100000 == min_dist:
        return -1
    return min_dist
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
