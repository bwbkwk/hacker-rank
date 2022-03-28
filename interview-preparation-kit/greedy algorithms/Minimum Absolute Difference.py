#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # negate the negative value by adding -1 * smallest
    smallest_x = min(arr)
    positive_arr = [x - smallest_x for x in arr]
    
    # sort the array as the minimum absolute different of an
    # integer x must be the number closest to them.
    positive_arr.sort()
    
    # set smallest to biggest number available
    smallest = int(sys.maxsize)
    
    # for every x in array check absolute different between 
    # number x+1 an x and update the smallest value
    for i in range(0,len(positive_arr)-1):
        dif = positive_arr[i+1] - positive_arr[i]
        if dif < smallest:
            smallest = dif
    return smallest
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
