import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or k == len(weights):
            return 0
        
        # Calculate the potential costs for each possible split point
        split_costs = [weights[i] + weights[i + 1] for i in range(len(weights) - 1)]
        
        # Sort the split costs
        split_costs.sort()
        
        # Calculate the minimum and maximum scores
        min_score = sum(split_costs[:k-1])
        max_score = sum(split_costs[-(k-1):])
        
        # Return the difference
        return max_score - min_score

def putMarbles(weights: List[int], k: int) -> int:
    return Solution().putMarbles(weights, k)