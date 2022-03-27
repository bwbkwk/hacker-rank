#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

# helper function to create every word and its number of occurences
# in a string
def buildCounter(string):
    C = Counter()
    for word in string:
        C[word] += 1
    return C

def checkMagazine(magazine, note):
    M,N = buildCounter(magazine),buildCounter(note)
    
    # for every word in note
    for word in N:
        # if word not availabe in M or the word needed in notes is bigger 
        # than in the magazine then the the kidnapper cant write the letter
        if word not in M or N[word] > M[word]:
            print("No")
            return
        
    print("Yes")
    return
    
            
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
