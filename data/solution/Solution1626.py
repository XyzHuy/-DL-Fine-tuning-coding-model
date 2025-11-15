import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Pair up ages and scores and sort by age, then by score
        players = sorted(zip(ages, scores))
        
        # Initialize the dp array where dp[i] represents the best team score ending with player i
        n = len(players)
        dp = [0] * n
        
        # The best team consisting of only one player is the player themselves
        for i in range(n):
            dp[i] = players[i][1]
        
        # Fill the dp array
        for i in range(1, n):
            for j in range(i):
                if players[i][1] >= players[j][1]:  # Only consider players with higher or equal scores
                    dp[i] = max(dp[i], dp[j] + players[i][1])
        
        # The answer is the maximum value in dp array
        return max(dp)

def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    return Solution().bestTeamScore(scores, ages)