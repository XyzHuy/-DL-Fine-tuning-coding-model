import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        if coins[-1] == -1:
            return []
        
        # Dynamic programming arrays
        dp = [float('inf')] * n
        parent = [-1] * n
        dp[-1] = coins[-1]
        
        for i in range(n-2, -1, -1):
            if coins[i] == -1:
                continue
            for k in range(1, maxJump + 1):
                if i + k < n:
                    if dp[i + k] < dp[i]:
                        dp[i] = dp[i + k]
                        parent[i] = i + k
            dp[i] += coins[i]
        
        # Reconstruct the path
        path = []
        i = 0
        while i != -1:
            path.append(i + 1)  # Convert 0-indexed to 1-indexed
            i = parent[i]
        
        return path if path[-1] == n else []

def cheapestJump(coins: List[int], maxJump: int) -> List[int]:
    return Solution().cheapestJump(coins, maxJump)