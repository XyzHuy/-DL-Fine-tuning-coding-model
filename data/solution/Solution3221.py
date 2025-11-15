import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[n-1] = 0  # No score if we are already at the last element
        
        # Traverse the array from the second last element to the first
        for i in range(n-2, -1, -1):
            max_score = 0
            for j in range(i+1, n):
                # Calculate the score for jumping from i to j
                score = (j - i) * nums[j] + dp[j]
                # Update the maximum score for the current position i
                max_score = max(max_score, score)
            dp[i] = max_score
        
        # The result is the maximum score starting from index 0
        return dp[0]

def maxScore(nums: List[int]) -> int:
    return Solution().maxScore(nums)