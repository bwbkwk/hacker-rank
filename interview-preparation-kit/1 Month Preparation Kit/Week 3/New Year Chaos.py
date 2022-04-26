#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    q = [i-1 for i in q]
    # print(q)
    bribeCnt = 0
    sIdx = 0
    for i in range(len(q)-1,0,-1):
        # print("Before",q)
        if q[i] == i:
            continue
        found = False
        for j in range(max(0,i-2),i):
            if q[j] > q[j+1]:
                found=True
                q[j], q[j+1] = q[j+1], q[j]
                bribeCnt+= 1
        if not found:
            print("Too chaotic")
            return
        # print("After",q)
        
    print("{0}".format(bribeCnt))
    # Write your code here

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
