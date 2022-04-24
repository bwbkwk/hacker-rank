#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

# note that this solution also works for the list of
# lonely integers.
def lonelyinteger(a):
    # create two set
    unq = set()
    nunq = set()
    
    for i in a:
        # if i occur in unq the it must be not unique
        if i in unq:
            nunq.add(i)
        else:
            unq.add(i)
    
    # find the unique element by find the different between
    # unq and nunq.
    return list(unq - nunq)[0]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
