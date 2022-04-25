#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    leftSum = 0
    rightSum = sum(arr)
    
    # foreach element as pivot
    for i in range(0,len(arr)):
        # remove element in index i from rightSum as 
        # it become a current pivot
        rightSum -= arr[i]
        if leftSum == rightSum:
            # print(arr[:i], arr[i+1:])
            return "YES"
        # add element in index i to leftSum 
        # for next iteration
        leftSum += arr[i]
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
