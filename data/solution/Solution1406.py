import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        @lru_cache(None)
        def dfs(index: int) -> int:
            if index == n:
                return 0
            if index > n:
                return float('-inf')
            
            # Calculate the maximum score Alice can achieve starting from index
            max_score = float('-inf')
            current_score = 0
            for i in range(index, min(index + 3, n)):
                current_score += stoneValue[i]
                max_score = max(max_score, current_score - dfs(i + 1))
            
            return max_score
        
        alice_score = dfs(0)
        if alice_score > 0:
            return "Alice"
        elif alice_score < 0:
            return "Bob"
        else:
            return "Tie"

def stoneGameIII(stoneValue: List[int]) -> str:
    return Solution().stoneGameIII(stoneValue)