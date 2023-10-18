#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    mx_topic, mx_team = 0, 0
    for i, p1 in enumerate(topic):
        for j in range(i+1,len(topic)):
            p2 = topic[j]
            p12 = '{0:b}'.format(int(p1,2) | int(p2,2))
            ct = Counter(p12)['1']
            if mx_topic > ct:
                continue
            if mx_topic == ct:
                mx_team += 1
                continue
            mx_topic = ct
            mx_team = 1
            
    return mx_topic, mx_team
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
