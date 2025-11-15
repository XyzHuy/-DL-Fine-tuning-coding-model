import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # Initialize a list to store the maximum length of subsequence for each sum up to target
        dp = [-1] * (target + 1)
        dp[0] = 0  # Base case: a sum of 0 can be achieved with an empty subsequence
        
        for num in nums:
            # Traverse the dp array backwards to avoid using the same number multiple times
            for j in range(target, num - 1, -1):
                if dp[j - num] != -1:
                    dp[j] = max(dp[j], dp[j - num] + 1)
        
        return dp[target]

def lengthOfLongestSubsequence(nums: List[int], target: int) -> int:
    return Solution().lengthOfLongestSubsequence(nums, target)