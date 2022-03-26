#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# naive solution
def arrayManipulationNaive(n, queries):
    L = [0]*n
    for q in queries:
        for i in range(q[0]-1,q[1]):
            L[i] += q[2]
    return max(L)

# efficient solution
def arrayManipulation(n, queries):
    L = [0]*(n+2)
    for q in queries:
        L[q[0]] += q[2]
        L[q[1]+1] += -q[2]
    maxVal = 0
    tempVal = 0
    print(L)
    for i in L[1:len(L)-1]:
        tempVal += i
        if tempVal > maxVal:
            maxVal = tempVal
    return maxVal


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
