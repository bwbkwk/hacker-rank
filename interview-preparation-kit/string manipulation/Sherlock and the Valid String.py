#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    # count occurence for every alphabet appear in string s
    cs = Counter(s)
    # count frequency of occurences
    freq = Counter([cs[k] for k in cs])
    
    # find the top 3 frequency
    most_common = freq.most_common(3)
    # print(most_common)
    
    # if only 1 alphabet appear return 'YES'
    if len(most_common) == 1:
        return "YES"
    # if 2 alphabet appear check the other condition
    if len(most_common) == 2:
        # if we can delete second alphabet as it only appear 1 return "YES"
        if most_common[1] == (1,1):
            return "YES"
        # if delete one character from string make it valid
        if abs(most_common[1][0] - most_common[0][0]) ==1 and most_common[1][1] == 1:
            return "YES"
    
    # otherwise return no
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
