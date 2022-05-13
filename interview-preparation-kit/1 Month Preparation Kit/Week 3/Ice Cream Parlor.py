#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    arr = [(arr[i],i+1) for i in range(len(arr))]
    arr.sort(key= lambda x: x[0])
    temp = []
    for item in arr:
        if item[0] > m:
            break
        temp.append(item)
    temp.reverse()
    
    # for readibility
    arr = temp
    
    options = dict()
    for item in arr:
        if item[0] in options:
            options[item[0]].append(item[1])
        else:
            options[item[0]] = [item[1]]
    
    for i in arr:
        complementaryPrice = m - i[0]
        if complementaryPrice in options.keys():
            if complementaryPrice != i[0]:
                res = [options[complementaryPrice][0],i[1]]
                res.sort()
                return res
            if len(options[i[0]]):
                res = options[i[0]]
                res.sort()
                return res[:2]
    
    return [-1,-1]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
