import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Initialize a dp array to store the minimum operations needed to make nums[0:i] beautiful
        dp = [0] * n
        
        # Calculate the initial operations needed for the first three elements
        for i in range(3):
            dp[i] = max(0, k - nums[i])
        
        # Fill the dp array for the rest of the elements
        for i in range(3, n):
            # The minimum operations needed to make nums[0:i] beautiful
            # is the minimum of the operations needed to make nums[0:i-1], nums[0:i-2], or nums[0:i-3] beautiful
            # plus the operations needed to make nums[i] at least k if it's not already
            dp[i] = min(dp[i-1], dp[i-2], dp[i-3]) + max(0, k - nums[i])
        
        # The answer is the minimum operations needed to make the entire array beautiful
        return min(dp[-1], dp[-2], dp[-3])

def minIncrementOperations(nums: List[int], k: int) -> int:
    return Solution().minIncrementOperations(nums, k)