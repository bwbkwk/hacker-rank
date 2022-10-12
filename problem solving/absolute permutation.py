#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    all_numbers = set(range(1,n+1))
    result = {}
    for i in range(1,n+1):
        if i in result:
            continue
        if i+k in all_numbers:
            all_numbers.remove(i+k)
            if i+k != i:
                all_numbers.remove(i)
            result[i] =i+k
            result[i+k] = i
        elif abs(i-k) in all_numbers:
            all_numbers.remove(abs(i-k))
            if abs(i-k) != i:
                all_numbers.remove(i)
            result[i] = abs(i-k)
            result[abs(i-k)] = i
        else:
            return [-1]
            
            
    return [result[i] for i in range(1,n+1)]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
