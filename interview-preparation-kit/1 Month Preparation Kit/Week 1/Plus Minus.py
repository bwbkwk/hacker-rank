#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    neg, pos, zero= 0, 0, 0
    for i in arr:
        if i == 0:
            zero +=1
        elif i > 0:
            pos +=1
        else:
            neg +=1
    size = len(arr)
    
    print(round(pos/size,4))
    print(round(neg/size,4))
    print(round(zero/size,4))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
