#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

# if the height of tower equal to 1 then P2 will win
# if the number of tower is even P2 always win by 
# mirroring the move on P1 and if the number of tower is
# odd the P1 always win as P1 can remove 1 tower height to 1
# and P1 will have a condition like P2 in the second condition
def towerBreakers(n, m):
    if m == 1:
        return 2
    if n % 2 == 0:
        return 2
    return 1
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
