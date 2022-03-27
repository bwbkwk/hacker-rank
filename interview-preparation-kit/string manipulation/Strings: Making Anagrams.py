#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#


# string x is longest anagram (thus requires minimum edit) 
# in a and b iff the use of every unique character 
# that constructing a & b is maximal. e.g. for string
# a = {x:2, y:3, z:1} and b = {x:2, y:2, z:0}
# we must use every character as maximal as possible that
# affordable by a & b. x = 2, y = 2 and z = 0
# by above definition we can find absolute difference from
# each character to find the minimum edit.
def makeAnagram(a, b):
    # count every possible character in a and b
    ca = Counter(a)
    cb = Counter(b)
    
    # get all unique character that constructing a and b
    all_c = set(ca.keys()).union(set(cb.keys()))
    
    dif = 0
    # for every unique character a union b
    # find the different of their occurence in a and b
    for c in all_c:
        dif += abs(ca[c] - cb[c])
    
    return dif

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
