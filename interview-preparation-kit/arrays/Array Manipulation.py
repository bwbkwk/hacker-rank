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
# to understand the concept just imagine you are draw
# a single line start with height 0 and most left position. 
# and for every query (s,e,v), you increase the height by v
# when you are in the position of s and keep drawing the line
# until you are in the position of e+1 you need to come back to
# the previous height before the addition of v by substracting it with v.     
def arrayManipulation(n, queries):
    L = [0]*(n+2)
    
    # for every query (s,e,v) put the value of v
    # in L[s] and put the negative value of v in L[e+1]
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
