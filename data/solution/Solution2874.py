import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Initialize arrays to store the maximum values
        max_from_left = [0] * n
        max_from_right = [0] * n
        
        # Fill max_from_left array
        max_from_left[0] = nums[0]
        for i in range(1, n):
            max_from_left[i] = max(max_from_left[i - 1], nums[i])
        
        # Fill max_from_right array
        max_from_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            max_from_right[i] = max(max_from_right[i + 1], nums[i])
        
        max_value = 0
        
        # Iterate through the array to find the maximum triplet value
        for j in range(1, n - 1):
            i_max = max_from_left[j - 1]
            k_max = max_from_right[j + 1]
            current_value = (i_max - nums[j]) * k_max
            max_value = max(max_value, current_value)
        
        return max_value

def maximumTripletValue(nums: List[int]) -> int:
    return Solution().maximumTripletValue(nums)