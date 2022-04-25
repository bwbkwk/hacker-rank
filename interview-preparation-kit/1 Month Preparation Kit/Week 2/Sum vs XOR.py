#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sumXor' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def sumXor(n):
    # corner case
    if n == 0:
        return 1
    # convert the number to its binary form
    s = "{0:b}".format(n)
    # count the occurence of zero in the binary form
    count_zero = 0
    for i in s:
        if i == '0':
            count_zero +=1
    # for each zero we can choose whether it can be 0 or 1 so
    # the every possibility can be count from the formula 2^count_zero
    return 2**count_zero
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumXor(n)

    fptr.write(str(result) + '\n')

    fptr.close()
