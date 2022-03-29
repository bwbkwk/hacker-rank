#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#


def whatFlavors(cost, money):
    
    cost_table = {}
    
    # enumerate every ice cream id in the cost table
    # with the key of its cost. Note: index notation start from 1
    for idx,c in enumerate(cost):
        cost_table[c] = cost_table.get(c,list())
        cost_table[c].append(idx+1)
    
    # for every possible price in cost table
    for k in cost_table:
        # calculate the money left after purchase ice cream
        # with cost of k
        money_left = money - k
        
        # check if the is any ice cream can be purchased 
        # with the money left.
        if money_left in cost_table:
            # check if the money left refers to the same item or
            # not when the money left equals to k
            if money_left == k and len(cost_table[k]) == 1:
                continue
                
            # get the icream id from cost_table with the key of k
            # and money_left 
            a = [cost_table[k].pop(), cost_table[money_left].pop()]
            
            # sort it in ascending order then print
            a.sort()
            print(a[0],a[1])
            break

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        money = int(input().strip())

        n = int(input().strip())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
