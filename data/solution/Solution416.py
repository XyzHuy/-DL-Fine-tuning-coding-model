import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # If the total sum is odd, it's not possible to partition it into two equal subsets
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        n = len(nums)
        
        # Initialize a DP array to keep track of possible sums
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: zero sum is always possible
        
        # Iterate over each number in the array
        for num in nums:
            # Traverse the dp array backwards
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]

def canPartition(nums: List[int]) -> bool:
    return Solution().canPartition(nums)