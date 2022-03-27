#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

# just brute force every possible combination since
# the array size is stricted into only 6x6
def hourglassSum(arr):
    maxHg = -sys.maxsize -1
    for j in range(0,6):
        for i in range(0,6):
            if i+2 > 5 or j+2 > 5:
                continue
            hg = sum([
                    sum(arr[j][i:i+3]), 
                    arr[j+1][i+1] ,
                    sum(arr[j+2][i:i+3])
                ]
            )
            if maxHg < hg:
                maxHg = hg
                
    return maxHg
            
                
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
