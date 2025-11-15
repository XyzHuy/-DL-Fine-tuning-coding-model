import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Step 1: Transform the input into earnings array
        max_num = max(nums)
        earnings = [0] * (max_num + 1)
        for num in nums:
            earnings[num] += num
        
        # Step 2: Initialize the dp array
        dp = [0] * (max_num + 1)
        dp[1] = earnings[1]
        
        # Step 3: Fill the dp array
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + earnings[i])
        
        # Step 4: The result is the last element in dp array
        return dp[max_num]

def deleteAndEarn(nums: List[int]) -> int:
    return Solution().deleteAndEarn(nums)