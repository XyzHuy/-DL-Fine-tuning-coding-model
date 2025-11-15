import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        # Compute prefix sums to quickly calculate the sum of any subarray
        prefix_sums = [0]
        for value in stoneValue:
            prefix_sums.append(prefix_sums[-1] + value)
        
        # Function to get the sum of stone values between indices left and right (inclusive)
        def get_sum(left, right):
            return prefix_sums[right + 1] - prefix_sums[left]
        
        # Memoized recursive function to determine the maximum score Alice can achieve
        @lru_cache(None)
        def dfs(left, right):
            if left >= right:
                return 0
            
            max_score = 0
            for i in range(left, right):
                left_sum = get_sum(left, i)
                right_sum = get_sum(i + 1, right)
                
                if left_sum < right_sum:
                    max_score = max(max_score, left_sum + dfs(left, i))
                elif left_sum > right_sum:
                    max_score = max(max_score, right_sum + dfs(i + 1, right))
                else:
                    max_score = max(max_score, left_sum + max(dfs(left, i), dfs(i + 1, right)))
            
            return max_score
        
        return dfs(0, len(stoneValue) - 1)

def stoneGameV(stoneValue: List[int]) -> int:
    return Solution().stoneGameV(stoneValue)