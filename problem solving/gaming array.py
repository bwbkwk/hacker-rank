#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def gamingArray(arr):
    l = [(x,i) for i,x in enumerate(arr)]
    l.sort(key= lambda x: x[0],reverse=True)
    
    temp = l[0][1]
    bob = True
    for i in range(1,len(l)):
        if l[i][1] > temp:
            continue
        bob = not bob
        temp = l[i][1]
    
    if bob:
        return "BOB"
    return "ANDY"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()
