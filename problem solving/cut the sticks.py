#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    
    left_stick = len(arr)
    cnt = Counter(arr)
    
    arr = [(k,cnt[k]) for k in cnt.keys()]
    arr = sorted(arr, key=lambda x: x[0])
    
    sticks = [left_stick]
    for _, v in arr:
        left_stick -= v
        sticks.append(left_stick)
        
    return sticks[:-1]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
