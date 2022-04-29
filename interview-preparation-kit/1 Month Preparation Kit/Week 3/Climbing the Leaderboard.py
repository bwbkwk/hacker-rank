#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

# 1st solution => linear search + set
def climbingLeaderboard_old1(ranked, player):
    sRanked = set(ranked)
    ranked = list(sRanked)
    ranked.append(-1)
    ranked.sort(reverse=True)
    playerRanks = []
    
    for score in player:
        for i in range(len(ranked)):
            if score >= ranked[i]:
                playerRanks.append(i+1)
                if score not in sRanked:
                    ranked.insert(i,score)
                    # print(ranked)
                    sRanked.add(score)
                break
        # print(ranked)
    return playerRanks

# 2nd solution => linear search + dictionary
def climbingLeaderboard_old2(ranked, player):
    ranked.append(-1)
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    leaderboard = {}
    for idx,r in enumerate(ranked):
        leaderboard[r] = idx+1
    # print(leaderboard)
    playerRanks = []
    for p in player:
        if p not in leaderboard:
            for i in range(len(ranked)):
                if p>ranked[i]:
                    leaderboard[p] = i
                    ranked.insert(i,p)
                    for j in range(i,len(ranked)):
                        leaderboard[ranked[j]] +=1
                    break
            # print(leaderboard)
            # print(ranked)
        playerRanks.append(leaderboard[p])
    return playerRanks

# 3rd solution => binary search
def climbingLeaderboard(ranked, player):
    ranked.append(-1)
    ranked = list(set(ranked))
    ranked.sort(reverse=True)
    
    playerRanks = []
    for p in player:
        l,h = 0,len(ranked)-1
        found = False
        while l <= h:
            m = (l + h)//2
            if ranked[m] > p:
                l = m + 1
            elif ranked[m] < p:
                h = m - 1
            else:
                found=True
                break
        if not found:
            if p < ranked[m]:
                m = m+1
            ranked.insert(m,p)
        
        playerRanks.append(m+1)
            
            
    return playerRanks
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
