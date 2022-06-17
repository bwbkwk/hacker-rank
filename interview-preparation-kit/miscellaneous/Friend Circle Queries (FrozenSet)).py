#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxCircle function below.
def maxCircle(queries):
    ans = []
    circles = set()
    biggest_circle = -1
    for query in queries:
        circle1 = frozenset([query[0]])
        for circle in circles:
            if query[0] in circle:
                 circle1 = circle
                 break
        circle2 = frozenset([query[1]])
        for circle in circles:
            if query[1] in circle:
                 circle2 = circle
                 break
        circles.discard(circle1)
        circles.discard(circle2)
        newSet = circle1.union(circle2)
        biggest_circle = max(biggest_circle,len(newSet))
        ans.append(biggest_circle)
        circles.add(newSet)
    return ans
        
        
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
