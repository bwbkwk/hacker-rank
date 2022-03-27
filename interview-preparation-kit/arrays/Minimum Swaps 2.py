#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

# for every i,x in list, the function work by 
# swap the value x if it is not i not equal to x <== second line (2)
# by doing so, you put x in its right position. 
# There is no better way to put x in its right position than only
# one swap if it is not in the correct position.
# then check the condition in the second line repeatedly
def minimumSwaps(arr):
    swapCtr = 0
    iHelper = 0
    i = 0
    while i < len(arr):
        if arr[i] == i+1:
            i+=1
            continue
        actualIndex = arr[i] - 1
        arr[i], arr[actualIndex] = arr[actualIndex], arr[i]
        swapCtr += 1
    return swapCtr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
