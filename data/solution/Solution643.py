import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initialize the sum of the first 'k' elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Use sliding window to find the maximum sum of any subarray of length 'k'
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)
        
        # The maximum average is the maximum sum divided by 'k'
        return max_sum / k

def findMaxAverage(nums: List[int], k: int) -> float:
    return Solution().findMaxAverage(nums, k)