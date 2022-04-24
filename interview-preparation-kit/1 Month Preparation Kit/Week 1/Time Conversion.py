#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    newHour = int(s[:2])
    if s[-2:] == 'PM':
        if newHour != 12:
            newHour = (newHour +12)
    else:
        newHour %= 12
    return "{:02d}:{}".format(newHour,s[3:-2])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
