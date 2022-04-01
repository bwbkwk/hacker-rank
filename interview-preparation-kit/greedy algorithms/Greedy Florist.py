#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.


# it's better to buy the most expensive
# first due to the price growth for the next
# buy so sort the flower price in descending
# order and buy the flower per person count
# and increase the price factor each iteration
def getMinimumCost(k, c):
    c.sort(reverse=True)
    
    pc = 0
    factor = 1
    total = 0
    
    while pc < len(c):
        total += factor * sum(c[pc : pc + k])
        pc += k
        factor += 1
        
    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
