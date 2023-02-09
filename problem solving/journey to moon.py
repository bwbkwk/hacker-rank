#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    countries = []
    processed = set()
    astronaut_index_processed = set()
    for i in range(0,n):
        if i in processed:
            continue
        country = set()
        q = [i]
        while len(q) > 0:
            p = q.pop(0)
            country.add(p)
            for index,pair in enumerate(astronaut):
                if index in astronaut_index_processed:
                    continue
                try:
                    p_pos = pair.index(p)
                except:
                    p_pos = -1
                if p_pos != -1:
                    q.append(pair[1-p_pos])
                    astronaut_index_processed.add(index)
            processed.add(p)
        countries.append(country)
    population = [len(country) for country in countries]
    
    total = 0
    for i in range(0,len(population)):
        for j in range(i+1,len(population)):
            total += population[i] * population[j]
    return total              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()
