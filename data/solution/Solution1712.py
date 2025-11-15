import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        
        # Calculate prefix sums
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
        
        total_ways = 0
        left_end = 0
        
        for left_end in range(n - 2):
            left_sum = prefix_sum[left_end]
            
            # Find the smallest mid_start such that left_sum <= mid_sum
            mid_start = left_end + 1
            while mid_start < n - 1 and left_sum > prefix_sum[mid_start] - prefix_sum[left_end]:
                mid_start += 1
            
            if mid_start >= n - 1:
                break
            
            # Find the largest mid_end such that mid_sum <= right_sum
            mid_end = mid_start
            while mid_end < n - 1 and prefix_sum[mid_end] - prefix_sum[left_end] <= prefix_sum[-1] - prefix_sum[mid_end]:
                mid_end += 1
            
            # All mid_start to mid_end - 1 are valid
            total_ways += mid_end - mid_start
            
            if total_ways >= MOD:
                total_ways %= MOD
        
        return total_ways % MOD

def waysToSplit(nums: List[int]) -> int:
    return Solution().waysToSplit(nums)