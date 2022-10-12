#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#
fibonnaci_table = dict()

def fibonnaciModified(n):
    if n in fibonnaci_table:
        return fibonnaci_table[n]
    fibonnaci_table[n] = fibonnaciModified(n-1)**2 + fibonnaciModified(n-2)
    return fibonnaci_table[n]

def fibonacciModified(t1, t2, n):
    fibonnaci_table[1] = t1
    fibonnaci_table[2] = t2
    
    res = fibonnaciModified(n)
    return res
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()
