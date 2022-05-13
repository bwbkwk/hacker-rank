#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    helper = []
    open_brackets = set(['{','[','('])
    complete_brackets = set(['{}','[]','()'])
    for bracket in s:
        if bracket in open_brackets:
            helper.append(bracket)
        else:
            if len(helper) == 0:
                return "NO"
            if helper.pop()+bracket not in complete_brackets: 
                return "NO"
        #print(helper)
    if len(helper) > 0:
        return "NO"
    return "YES"
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
