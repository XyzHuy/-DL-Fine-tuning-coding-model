import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to store the maximum sum and the current sum
        max_sum = current_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Update the current sum to be the maximum of the current number or the current sum plus the current number
            current_sum = max(num, current_sum + num)
            # Update the maximum sum if the current sum is greater
            max_sum = max(max_sum, current_sum)
        
        return max_sum

def maxSubArray(nums: List[int]) -> int:
    return Solution().maxSubArray(nums)