import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        # Initialize include and exclude arrays
        include = [0] * n
        exclude = [0] * n
        
        # Base case for the first element
        include[0] = max(0, nums[0])
        exclude[0] = 0
        
        # Fill the include and exclude arrays for the initial nums
        for i in range(1, n):
            include[i] = exclude[i-1] + max(0, nums[i])
            exclude[i] = max(include[i-1], exclude[i-1])
        
        # Function to update the include and exclude arrays after a query
        def update(pos, new_val):
            old_val = nums[pos]
            nums[pos] = new_val
            
            # Update the include and exclude values starting from pos
            if pos == 0:
                include[pos] = max(0, nums[pos])
                exclude[pos] = 0
            else:
                include[pos] = exclude[pos-1] + max(0, nums[pos])
                exclude[pos] = max(include[pos-1], exclude[pos-1])
            
            for i in range(pos + 1, n):
                include[i] = exclude[i-1] + max(0, nums[i])
                exclude[i] = max(include[i-1], exclude[i-1])
        
        total_sum = 0
        for pos, xi in queries:
            update(pos, xi)
            total_sum = (total_sum + max(include[-1], exclude[-1])) % MOD
        
        return total_sum

def maximumSumSubsequence(nums: List[int], queries: List[List[int]]) -> int:
    return Solution().maximumSumSubsequence(nums, queries)