#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

# just normal bubble sort with swap counter
def countSwaps(a):
    len_a = len(a)
    swapCtr = 0
    
    for i in range(0,len_a):
        for j in range(0,len_a-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapCtr+= 1
    
    print("Array is sorted in {n} swaps.".format(n=swapCtr))
    print("First Element: {first}".format(first=a[0]))
    print("Last Element: {last}".format(last=a[-1]))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
