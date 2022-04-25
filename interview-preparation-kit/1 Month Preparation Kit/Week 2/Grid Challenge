#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    nGrid = []
    # sort each row
    for row in grid:
        nLine = list(row)
        nLine.sort()
        nGrid.append(nLine)
    
    # check foreach column if alphabet in the index of x has
    # alphabetical order lower than x-1, return "NO"
    for i in range(0,len(nGrid[0])):
        for j in range(1,len(nGrid)):
            if nGrid[j-1][i] > nGrid[j][i]:
                return "NO"
    return "YES" 
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
