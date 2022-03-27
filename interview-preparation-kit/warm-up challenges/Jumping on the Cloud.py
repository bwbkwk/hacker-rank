#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # init initial position and jump counter to zero
    pos, jump = 0, 0
    
    # while not in the finish line
    while pos != len(c)-1:
        # just jump block, so 
        pos += 1
        # but if it possible, then jump by 2
        if pos + 1 < len(c) and c[pos+1] == 0:
            pos += 1
        # add jump counter
        jump+=1
        print(pos, jump)
    
    return jump
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
