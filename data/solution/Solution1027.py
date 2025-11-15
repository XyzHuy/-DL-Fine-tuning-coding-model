import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        
        # Dictionary to store the length of arithmetic subsequences
        # dp[i][d] will store the length of the arithmetic subsequence ending at index i with difference d
        dp = [{} for _ in range(n)]
        max_length = 2
        
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2  # At least two elements: nums[j] and nums[i]
                
                max_length = max(max_length, dp[i][diff])
        
        return max_length

def longestArithSeqLength(nums: List[int]) -> int:
    return Solution().longestArithSeqLength(nums)