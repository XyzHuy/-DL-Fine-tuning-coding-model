import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        # Create a dictionary to store the longest chain ending with each number
        dp = defaultdict(int)
        
        # Sort the numbers to process them in increasing order
        nums.sort()
        
        # Iterate over each number in the sorted list
        for num in nums:
            # We can either take the number as is or increment it by 1
            # Update the dp entry for num + 1 by considering the chain ending with num
            dp[num + 1] = max(dp[num + 1], dp[num] + 1)
            # Update the dp entry for num by considering the chain ending with num - 1
            dp[num] = max(dp[num], dp[num - 1] + 1)
        
        # The result is the maximum value in the dp dictionary
        return max(dp.values())

def maxSelectedElements(nums: List[int]) -> int:
    return Solution().maxSelectedElements(nums)