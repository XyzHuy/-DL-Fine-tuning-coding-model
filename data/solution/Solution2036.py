import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumAlternatingSubarraySum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        max_sum = nums[0]
        even_sum = nums[0]  # Sum when the current element is at an even index
        odd_sum = float('-inf')  # Sum when the current element is at an odd index
        
        for i in range(1, len(nums)):
            # Update odd_sum and even_sum based on the current element
            new_odd_sum = even_sum - nums[i]
            new_even_sum = max(odd_sum + nums[i], nums[i])
            
            # Update the maximum sum found so far
            max_sum = max(max_sum, new_odd_sum, new_even_sum)
            
            # Update even_sum and odd_sum for the next iteration
            even_sum = new_even_sum
            odd_sum = new_odd_sum
        
        return max_sum

def maximumAlternatingSubarraySum(nums: List[int]) -> int:
    return Solution().maximumAlternatingSubarraySum(nums)