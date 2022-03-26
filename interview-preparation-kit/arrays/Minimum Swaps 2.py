#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
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
