#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def rotate_character(c,k,islower=False):
    ed = 90
    if islower:
        ed = 122
    nc = ord(c) +k
    if nc > ed:
        nc-=26
    return chr(nc)
    


def caesarCipher(s, k):
    res = []
    # mod by 26 as with k of 26, the input and output string
    # will be the same. 
    k %= 26
    for c in s:
        if c.isalpha():
            res.append(rotate_character(c,k,c.islower()))
        else:
            res.append(c)
            
    return ''.join(res)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
