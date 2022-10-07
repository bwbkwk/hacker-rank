#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    cnt = Counter(a)
    keys = list(cnt.keys())
    keys.sort()
    max_subarr = cnt.most_common()[0][1]
    for i in range(0,len(keys)-1):
        if keys[i+1] == keys[i] + 1:
            max_subarr = max(max_subarr, cnt[keys[i]]+cnt[keys[i]+1])
    return max_subarr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
