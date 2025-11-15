import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        # Create a dictionary to map suffixes to their respective costs
        suffix_costs = {}
        for word, cost in zip(words, costs):
            if word in suffix_costs:
                suffix_costs[word] = min(suffix_costs[word], cost)
            else:
                suffix_costs[word] = cost
        
        @lru_cache(None)
        def dp(i):
            if i == 0:
                return 0
            min_cost = float('inf')
            for word, cost in suffix_costs.items():
                if i >= len(word) and target[i-len(word):i] == word:
                    min_cost = min(min_cost, cost + dp(i - len(word)))
            return min_cost
        
        result = dp(len(target))
        return result if result != float('inf') else -1

def minimumCost(target: str, words: List[str], costs: List[int]) -> int:
    return Solution().minimumCost(target, words, costs)