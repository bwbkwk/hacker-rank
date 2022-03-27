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
    L = list(reversed(range(0,len(q))))
    swapCtrAcc = 0
    for i in L:
        if q[i] == i+1:
            continue
        for x in range(max(0,i-2),i):
            if q[x+1] > q[x]:
                continue
            q[x], q[x+1] = q[x+1], q[x]
            swapCtrAcc += 1
        if q[i] != i+1:
            print("Too chaotic")
            return
    print(swapCtrAcc)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
