#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    # Counter is just like a dictionary data type for
    # counting occurences of its key (key, counter)
    freq = Counter()
    group = Counter()
    outputs = []
    for query in queries:
        if query[0] == 1:
            # when new data x inserted, it left the group of its old freq,
            group[freq[query[1]]] -= 1
            # it freq increased by 1
            freq[query[1]] +=1
            # it join new group of its new freq
            group[freq[query[1]]] += 1
        elif query[0] == 2:
            # when data x is deleted, he left his current freq group,
            group[freq[query[1]]] -= 1
            # it freq decreased by 1
            freq[query[1]] -=1
            # no deletion if data frequencies below 0 (data not found)
            freq[query[1]] = max(0,freq[query[1]])
            # it join new group of its new freq
            group[freq[query[1]]] += 1  
        else:
            #if group with freq x exist return 1, otherwise return 0
            output = 1 if group[query[1]] > 0 else 0
            outputs.append(output)
        # for debugging purposes, to make it easier to understand
        # print(freq)
        # print(group)
    return outputs 
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
