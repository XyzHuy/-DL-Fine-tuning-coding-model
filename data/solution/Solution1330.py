import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        initial_value = 0
        
        # Calculate the initial value of the array
        for i in range(n - 1):
            initial_value += abs(nums[i] - nums[i + 1])
        
        # Consider reversing subarrays that include the first element
        max_edge_reverse = 0
        for i in range(1, n):
            max_edge_reverse = max(max_edge_reverse, abs(nums[0] - nums[i]) - abs(nums[i] - nums[i - 1]))
        
        # Consider reversing subarrays that include the last element
        for i in range(n - 1):
            max_edge_reverse = max(max_edge_reverse, abs(nums[n - 1] - nums[i]) - abs(nums[i + 1] - nums[i]))
        
        # Consider reversing internal subarrays
        max_internal_reverse = 0
        min_pair = float('inf')
        max_pair = float('-inf')
        
        for i in range(n - 1):
            # Track the minimum of max(nums[i], nums[i+1]) and maximum of min(nums[i], nums[i+1])
            min_pair = min(min_pair, max(nums[i], nums[i + 1]))
            max_pair = max(max_pair, min(nums[i], nums[i + 1]))
        
        # The maximum increase from internal reversal is 2 * (max_pair - min_pair)
        max_internal_reverse = 2 * max(0, max_pair - min_pair)
        
        # The result is the initial value plus the maximum possible increase
        return initial_value + max(max_edge_reverse, max_internal_reverse)

def maxValueAfterReverse(nums: List[int]) -> int:
    return Solution().maxValueAfterReverse(nums)