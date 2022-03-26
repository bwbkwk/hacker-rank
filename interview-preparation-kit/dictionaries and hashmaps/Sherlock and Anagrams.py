#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def generateSubstringDict(s):
    len_s = len(s)
    S = [s[i:j] for i in range(len_s) for j in range(i+1,len_s+1)]
    
    # make Counter to frozenset make it can be used as dictionary key
    dictArr = [frozenset(Counter(s).items()) for s in S]
    return dictArr

# solution 1 (TLE)
def sherlockAndAnagrams_1(s):
    substrs = generateSubstringDict(s)
    
    #print(substrs)
    
    anagram_count = 0
    len_substrs =len(substrs)
    substrs_length_table = [len(substr) for substr in substrs]
        
    for i in range(len_substrs):
        for j in range(i+1,len_substrs):
            if substrs_length_table[i] != substrs_length_table[j]:
                continue
            if substrs[i] == substrs[j]:
                # print(substrs[i],",",substrs[j])
                anagram_count+= 1
    return anagram_count

# solution 2 
def sherlockAndAnagrams(s):
    substrs = generateSubstringDict(s)
    
    # print(substrs)
    
    map = {}
    
    for substr in substrs:
        map[substr] = map.get(substr,0) + 1
    
    anagram_count = 0
    
    for k in map:
        # formula all possible combination from map[k] count
        # example, for value of 4 (1,2,3,4)
        # the combination is given by (1,2), (1,3), (1,4) = 3
        # plus (2,3), (2,4) = 2 and plus (3,4) = 1
        # 3 + 2 + 1 = 4 * 3 /2
        anagram_count += (map[k] * (map[k]-1))//2
    return anagram_count
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')
        print("================")

    fptr.close()
