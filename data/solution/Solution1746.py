import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # Initialize variables to store the maximum subarray sum without and with the operation
        max_ending_here_no_op = nums[0]
        max_ending_here_with_op = nums[0] * nums[0]
        max_so_far = max_ending_here_with_op
        
        for i in range(1, n):
            # Update max_ending_here_with_op considering the current element squared or adding to the previous subarray with operation
            max_ending_here_with_op = max(
                max_ending_here_no_op + nums[i] * nums[i],  # Start new subarray with operation at current element
                max_ending_here_with_op + nums[i],          # Continue subarray with operation
                nums[i] * nums[i]                           # Start new subarray with operation at current element
            )
            
            # Update max_ending_here_no_op for the current element
            max_ending_here_no_op = max(
                max_ending_here_no_op + nums[i],  # Continue subarray without operation
                nums[i]                           # Start new subarray without operation
            )
            
            # Update the overall maximum sum found so far
            max_so_far = max(max_so_far, max_ending_here_with_op)
        
        return max_so_far

def maxSumAfterOperation(nums: List[int]) -> int:
    return Solution().maxSumAfterOperation(nums)