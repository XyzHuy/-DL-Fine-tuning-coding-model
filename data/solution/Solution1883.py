import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(n)]
        dp[0][0] = dist[0]
        
        for i in range(1, n):
            # Without any skips for the first i+1 roads
            dp[i][0] = (dp[i-1][0] // speed + (1 if dp[i-1][0] % speed != 0 else 0)) * speed + dist[i]
            for j in range(1, i + 1):
                # Case 1: Skip the rest after the i-th road
                dp[i][j] = dp[i-1][j-1] + dist[i]
                # Case 2: Do not skip the rest after the i-th road
                dp[i][j] = min(dp[i][j], (dp[i-1][j] // speed + (1 if dp[i-1][j] % speed != 0 else 0)) * speed + dist[i])
        
        for j in range(n):
            if dp[n-1][j] <= speed * hoursBefore:
                return j
        return -1

def minSkips(dist: List[int], speed: int, hoursBefore: int) -> int:
    return Solution().minSkips(dist, speed, hoursBefore)