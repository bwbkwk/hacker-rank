#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

# just sort the price in ascending order and 
# init temporary sum to zero, loop every price 
# and if the price still affordable (temporary sum <= k)
# add it to temporary sum and go to the next item
def maximumToys(prices, k):
    prices = sorted(prices)
    
    temp_k = 0
    item_count = 0
    for price in prices:
        if temp_k + price > k:
            break
        temp_k += price
        item_count += 1
    return item_count
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
