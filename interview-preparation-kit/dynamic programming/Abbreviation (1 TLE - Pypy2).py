#!/bin/python

import os
import sys

#
# Complete the 'abbreviation' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

dp = {}

def abbreviation(a, b):
    key = a +' '+ b
    if key in dp:
        return dp[key]
    if len(a) < len(b):s
        dp[key] = False
        return False
    if a == b:
        dp[key] = True
        return True
    if len(b) == 0:
        dp[key] = a.islower() 
        return dp[key]
    if a[0] == b[0]:
        dp[key] = abbreviation(a[1:],b[1:])
        return dp[key]
    if a[0].isupper():
        dp[key] = False
        return False
     
    if a[0].upper() != b[0]:
        dp[key] = abbreviation(a[1:],b)
        return dp[key]
    dp[key] = abbreviation(a[1:],b) or abbreviation(a[1:],b[1:]) 
    return dp[key]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        a = raw_input()

        b = raw_input()

        result = abbreviation(a, b)
        
        fptr.write('YES\n' if result else 'NO\n')

    fptr.close()
