#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    X = [1 if c == 'U' else -1 for c in path]
    sl = 0
    v = 0
    oldSl = 0
    for i in X:      
        sl += i
        # print("SL: ",sl, "Old SL:",oldSl)
        if sl == -1 and oldSl == 0:
            v += 1
            # print(v)
        oldSl = sl
    return v
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
