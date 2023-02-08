#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#

def bigSorting_simple(unsorted):
    arr = [int(x) for x in unsorted]
    arr.sort()
    return [str(x) for x in arr]


def bigSorting_sort_per_length(unsorted):
    by_length = dict()
    for x in unsorted:
        lnx = len(x)
        if lnx not in by_length:
            by_length[lnx] = [int(x)]
        else:
            by_length[lnx].append(int(x))
    for lnx in by_length:
        by_length[lnx].sort()
    
    res = []
    for lnx in sorted(by_length.keys()):
        res += by_length[lnx]
    return [str(x) for x in res]

def bigSorting(unsorted):
    return sorted(unsorted, key = lambda s: int(s))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
