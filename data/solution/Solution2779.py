import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # Sort the array to facilitate the sliding window approach
        nums.sort()
        
        left = 0
        max_beauty = 0
        
        # Use a sliding window to find the maximum length of a subsequence
        for right in range(len(nums)):
            # Check if the current window is valid
            while nums[right] - nums[left] > 2 * k:
                left += 1
            # Update the maximum beauty
            max_beauty = max(max_beauty, right - left + 1)
        
        return max_beauty

def maximumBeauty(nums: List[int], k: int) -> int:
    return Solution().maximumBeauty(nums, k)