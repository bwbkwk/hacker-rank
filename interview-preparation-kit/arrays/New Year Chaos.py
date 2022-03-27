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

# start from right to left, for every n in queue q just do swap 
# from q[n-2] to q[n-1] and q[n-1] to q[n], if the value on the
# left is greater than the right. after the swap check whether 
# q[n] equal to n if no it is to chaotic since n must be bribe 
# more than 2 times. also, dont forget to count every swap!
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
