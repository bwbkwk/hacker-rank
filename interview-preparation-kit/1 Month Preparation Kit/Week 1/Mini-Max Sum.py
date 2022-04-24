#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # min value must be obtained from 4 smallest value from the array
    # and 4 largest value for the max. Thus, sort the array from the
    # ascending order to find the smallest and largest value
    arr.sort()
    print(sum(arr[:4]), sum(arr[-4:]))
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
