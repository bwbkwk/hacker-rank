#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    flippedN = ''.join(
        # print the number using its binary format (b)
        # with 32 leading zeros and flip each character
        ['1' if c == '0' else '0' for c in "{0:032b}".format(n)]
    )
    
    # return the integer representation of the binary
    return int(flippedN, 2)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
