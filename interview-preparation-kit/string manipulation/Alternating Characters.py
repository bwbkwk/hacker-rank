#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    runningChar = s[0]
    runningIdx = 0
    deletion = 0
    for idx,c in enumerate(s[1:]):
        # everytime we got the same character as before
        # add running index
        if runningChar == c:
            runningIdx += 1
        # if we got different character add runningIndex to
        # deletion counter, reset running index and character
        else:
            deletion += runningIdx
            runningChar = c
            runningIdx = 0
            
    # add last running index
    deletion += runningIdx
    return deletion
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
