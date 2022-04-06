#!/bin/python3

import math
import os
import random
import re
import sys

def maxSubsetSum(arr): 
    # negate negative value to zero so we can simplify
    # the loop (do not need to put arr[i] and dp[i-2]
    # in the max function).
    arr = [max(0,x) for x in arr]
    
    # create helper to count the max value for sub array
    # starting from zero and one
    dp = {}
    # for index zero, just put the value to helper
    # and for one, the max can be count using max from
    # 0 and 1. if value in index 0 bigger then choose it
    # otherwise choose value in index 0. (remember that we
    # can only choose one index because of non-adjacent 
    # constraint)
    dp[0], dp[1] = arr[0], max(arr[0],arr[1])
    
    # for every sub arry with the length of i, we can choose
    # which value is bigger, the precomputed max value on the 
    # left adjacent or the value in index i + precomputed max 
    # value for subarray with length i-2 
    for i in range(2,len(arr)):
        dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    
    # return the result as computed max value for the last
    # element in the array contain the max sub array for the 
    # given input.
    return dp[len(arr)-1]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
