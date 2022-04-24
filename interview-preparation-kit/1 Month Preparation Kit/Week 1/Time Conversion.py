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
    # get the hour
    newHour = int(s[:2])
    # get the last 2 character and check whether is AM or PM
    if s[-2:] == 'PM':
        # if newHour not equal to 12 add 12 hour so it follows
        # 24-hour system
        if newHour != 12:
            newHour = (newHour +12)
    else:
        # mod by 12 so if the hour is 12 it become 00.
        newHour %= 12
    return "{:02d}:{}".format(newHour,s[3:-2])
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
