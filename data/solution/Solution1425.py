import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = nums[:]  # Initialize dp array with the same values as nums
        dq = deque()  # Deque to store indices of dp array
        
        for i in range(n):
            # The current dp[i] is the maximum of nums[i] and nums[i] + the maximum of the previous dp values within the window of size k
            if dq:
                dp[i] = max(dp[i], dp[dq[0]] + nums[i])
            
            # Maintain the deque in decreasing order of dp values
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            
            # Add the current index to the deque
            dq.append(i)
            
            # Remove the index from the deque if it is out of the window of size k
            if dq[0] == i - k:
                dq.popleft()
        
        return max(dp)

def constrainedSubsetSum(nums: List[int], k: int) -> int:
    return Solution().constrainedSubsetSum(nums, k)