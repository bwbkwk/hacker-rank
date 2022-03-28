#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

def activityNotifications(expenditure , d):
    # count frequency of each expenditure from index 0 to d -1
    freq = Counter(expenditure[:d])
    
    # formula to calculate median times two
    def medianT2():
        # init median position is d//2
        # for 4 and 5 data the value will be 2
        medPos = d//2
        
        # correct median position if d is odd
        # median position of 5 data is the data number 3
        if d % 2 == 1:
            medPos += 1
        
        ctr, i = 0, 0
        # find the median for the case of odd value of d
        # and find the first/ left median for the case of
        # even value of d 
        for i in range(0,201):
            if i in freq:
                ctr += freq[i]
            if ctr >= medPos:
                break
        
        # if d is odd return the two value of median or
        # for the case of even value of d, if counter value 
        # is higher than medPos, this means second/ right median
        # is also i
        if d % 2 == 1 or ctr > medPos:
            return i + i
        
        # find the second median if not already covered 
        # by ctr value
        j = 0
        for j in range(i+1,201):
            if j in freq:
                break
            
        # return the value of first and second median
        return i + j
                
    fraud = 0
    for i in range(d,len(expenditure)):
        if expenditure[i] >= medianT2():
            fraud += 1
        # update the frequency table remove the most left expenditure
        # and add the current expenditure to be used by next
        freq[expenditure[i-d]] -= 1
        freq[expenditure[i]] +=1
    return fraud

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
