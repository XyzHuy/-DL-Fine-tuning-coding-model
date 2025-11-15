import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        min_cost = float('inf')
        
        # Iterate over the number of rotations
        for k in range(n):
            current_cost = k * x
            # Calculate the cost of collecting chocolates with k rotations
            for i in range(n):
                current_cost += min(nums[(i - j) % n] for j in range(k + 1))
            # Update the minimum cost
            min_cost = min(min_cost, current_cost)
        
        return min_cost

def minCost(nums: List[int], x: int) -> int:
    return Solution().minCost(nums, x)