#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

number_to_word = {
    0: 'o\' clock',
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'quarter',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'half'
}

def timeInWords(h, m):
    hour_part = "{}"
    conjunction_part = "{}"
    minute_part = "{}"
    final_format = "{m}{ms}{c} {h}"
    if m == 0:
        conjunction_part = conjunction_part.format("")
        final_format="{h} {m}"
    elif m > 30:
        h = max(h+1%13,1)
        conjunction_part = conjunction_part.format(" to")
        m = 60 - m
    else:
        conjunction_part = conjunction_part.format(" past")
    
    hour_part = hour_part.format(number_to_word[h])
    
    if m in number_to_word:
        minute_part = number_to_word[m]
    else:
        minute_part = number_to_word[(m//10)*10] + " "+ number_to_word[m%10]
    
    result = ""
    minute_desc = ""
    if m == 0 or m == 15 or m == 30:
        minute_desc = ""
    elif m == 1:
        minute_desc = " minute"
    else:
        minute_desc = " minutes"
    result = final_format.format(m=minute_part,ms=minute_desc, h=hour_part, c=conjunction_part)   
    return result
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
