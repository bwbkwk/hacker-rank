#!/bin/python3

import math
import os
import random
import re
import sys 
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # reverse the element in array since we must
    # have freq of x * r to count freq of pairs (x, x * r) and triplets
    arr = reversed(arr)
    
    # create two Counter to count freq of elements and pairs
    elFreq, pairsFreq = Counter(), Counter()
    
    # init triplets counters to 0, don't need to create Counter data
    # structure since we just need to get total occurences of every possible
    # triplet
    counter = 0
    
    
    for el in arr:
        biggerEl = el * r
        if biggerEl in pairsFreq:
             counter += pairsFreq[biggerEl]
        if biggerEl in elFreq:
            pairsFreq[el] += elFreq[biggerEl]
        elFreq[el] += 1
        # print(elFreq)
        # print(pairsFreq)
    return counter
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

    
