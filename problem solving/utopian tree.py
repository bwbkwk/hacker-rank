#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
utopianTrees = dict()
utopianTrees[0] = 1
def utopianTree(n):
    if n in utopianTrees:
        return utopianTrees[n]
    
    if n % 2 == 0:
        utopianTrees[n] = 1 + utopianTree(n-1)
        return utopianTrees[n]
    
    utopianTrees[n] = 2 * utopianTree(n-1)
    return utopianTrees[n]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
