import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = nums.count(1)
        
        # If there are no 1's or all are 1's, no swaps are needed
        if total_ones == 0 or total_ones == n:
            return 0
        
        # Create a doubled array to handle the circular nature
        doubled_nums = nums + nums
        
        # Initial count of 1's in the first window of size `total_ones`
        current_ones = doubled_nums[:total_ones].count(1)
        min_swaps = total_ones - current_ones
        
        # Slide the window over the doubled array
        for i in range(1, n):
            # Slide the window: remove the first element and add the next element
            current_ones -= doubled_nums[i - 1]
            current_ones += doubled_nums[i + total_ones - 1]
            # Calculate the minimum swaps needed
            min_swaps = min(min_swaps, total_ones - current_ones)
        
        return min_swaps

def minSwaps(nums: List[int]) -> int:
    return Solution().minSwaps(nums)