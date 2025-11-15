import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
import sys

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Step 1: Create a mapping from substring to its index
        id = {}
        for x in original + changed:
            if x not in id:
                id[x] = len(id)
        
        n = len(id)
        # Step 2: Initialize the distance matrix with infinity
        dist = [[sys.maxsize] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # Step 3: Populate the distance matrix with given costs
        for x, y, c in zip(original, changed, cost):
            i, j = id[x], id[y]
            dist[i][j] = min(dist[i][j], c)
        
        # Step 4: Use Floyd-Warshall to find all pairs shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] < sys.maxsize and dist[k][j] < sys.maxsize:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Step 5: Dynamic Programming to find the minimum cost to convert source to target
        m = len(source)
        dp = [sys.maxsize] * (m + 1)
        dp[0] = 0
        
        for i in range(1, m + 1):
            for j in range(i):
                sub_s = source[j:i]
                sub_t = target[j:i]
                if sub_s == sub_t:
                    dp[i] = min(dp[i], dp[j])
                elif sub_s in id and sub_t in id:
                    dp[i] = min(dp[i], dp[j] + dist[id[sub_s]][id[sub_t]])
        
        return dp[m] if dp[m] < sys.maxsize else -1

def minimumCost(source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    return Solution().minimumCost(source, target, original, changed, cost)