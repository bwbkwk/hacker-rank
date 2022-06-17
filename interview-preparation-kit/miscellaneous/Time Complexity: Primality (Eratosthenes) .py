#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primality' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

primes = []

def calculateAllPrimes():
    idx = 2
    while idx < len(primes):
        if not primes[idx]:
            idx+=1
            continue
        not_prime = idx*idx
        while not_prime < len(primes):
            primes[not_prime] = False
            not_prime += idx
        idx+= 1
    return

def primalityOld(n):
    if primes[n]:
        return "Prime"
    else:
        return "Not prime"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())
    ns, mx = [], -1
    for p_itr in range(p):
        n = int(input().strip())
        ns.append(n)
        mx = max(mx, n)
    primes = [True] * (mx + 1)
    primes[0] = False
    primes[1] = False
    calculateAllPrimes()
    for n in ns:
        result = primality(n)
        fptr.write(result + '\n')

    fptr.close()
