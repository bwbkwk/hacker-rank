#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#
number = 2
helper = []
for i in range(63):
    helper.append(number)
    number *=2

def search(x):
    for i in range(len(helper)):
        if helper[i] > x:
            return helper[i-1]
    return helper[-1]

def counterGame(n):
    # if n equals to one then Richard win
    if n == 1:
        return "Richard"
    # even turn for Louise and odd for Richard,
    # start by Louise turn
    turn = 0
    while(True):
        # search the nearest power of two to n
        h = search(n)
        # if the nearest power of two to n is n then
        if h == n:
            n //= 2
        # otherwise substract it to n
        else:
            n -= h
        # the end of game case
        if n == 1:
            break
        turn+=1
    if turn % 2 == 1:
        return "Richard"
    return "Louise"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()
