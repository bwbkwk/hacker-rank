#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    ls = []
    
    for i in range(p,q+1):
        si = str(i)
        lsi = len(si)
        si2 = str(i**2)
        r = si2[-lsi:]
        l =  si2[:len(si2)-lsi]
        if l == '':
            l = '0'
        if i == int(r) + int(l):
            ls.append(si)
    if len(ls) == 0:
        print('INVALID RANGE')
    print(' '.join(ls))
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
