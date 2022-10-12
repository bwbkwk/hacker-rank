#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    text = [c for c in s if c != ' ']
    len_squared = math.sqrt(len(text))
    col, row = math.ceil(len_squared), math.floor(len_squared)
    res = []
    while col * row < len(text):
        if row > col:
            col += 1
        else:
            row += 1
    print(col,row)
    for c in range(0,col):
        for r in range(0,row):
            i = r * col+ c
            if i >= len(text):
                break
            res.append(text[i])
        res.append(' ')
    return ''.join(res)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
