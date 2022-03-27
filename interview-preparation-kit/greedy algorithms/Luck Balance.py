#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    important_contest = []
    
    unimportant_score = 0
    
    # lose all unimportant one while keep track all
    # the important contest
    for contest in contests:
        if contest[1] == 1:
            important_contest.append(contest[0])
            continue
        unimportant_score += contest[0]
    
    # sort important contest score from high to low
    important_contest.sort(reverse=True)
    
    # lose all the highest to maximize the gain and
    # win the rest
    return unimportant_score - sum(important_contest[k:]) + sum(important_contest[:k]) 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
