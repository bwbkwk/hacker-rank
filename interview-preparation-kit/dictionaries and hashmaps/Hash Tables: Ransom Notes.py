#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#
def buildDictionary(string):
    D = dict()
    for word in string:
        if word in D:
            D[word] += 1
        else:
            D[word] = 1
    return D

def checkMagazine(magazine, note):
    M,N = buildDictionary(magazine),buildDictionary(note)
    
    for word in N:
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
