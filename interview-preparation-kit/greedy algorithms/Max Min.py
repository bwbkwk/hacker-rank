#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # sort the array to make the problem easier
    arr.sort()
    # set the smallest distance 
    smallest = int(sys.maxsize)
    
    # for every position x and x+k within the sorted array 
    # just count the distance between the number in
    # position of x with x+k since x will be the 
    # smallest number and x+k will be the highest
    # and we dont need to count the number of
    # x with x+k + [1 or 2 or ...] and the number of 
    # x - [1 or 2 or ...] with x+k because distance of x and x+k 
    # will be the smallest
    for i in range(0,len(arr)-k+1):
        smallest = min([smallest,arr[i+k-1] - arr[i]])
    return smallest
            
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
