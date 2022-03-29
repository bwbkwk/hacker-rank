#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# based on the given example and some calculations
# value of 1 is 1, (given by the example)
# value of 2 is 2 [(1,1) and (2)]
# value of 3 is 4, (given by the example)
# value of 4 is 7, consists of
# [(1,1,1,1), (1,1,2), (1,2,1), (2,1,1), (2,2), (3,1), (1,3)]
# value of 5 is 13 (given by the example) 

# we can observe a pattern where value of n is build based on
# sum of (n-1, n-2, n-3)
table = {1:1,2:2,3:4}
def stepPerms(n):
    if n in table:
        return table[n]
    table[n] = stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)
    return table[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        n = int(input().strip())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
