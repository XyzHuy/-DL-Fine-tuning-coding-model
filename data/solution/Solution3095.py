import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_length = float('inf')
        
        # Iterate over all possible starting points of subarrays
        for start in range(n):
            current_or = 0
            # Iterate over all possible ending points of subarrays starting from 'start'
            for end in range(start, n):
                current_or |= nums[end]
                # Check if the current subarray is special
                if current_or >= k:
                    min_length = min(min_length, end - start + 1)
                    break  # No need to check longer subarrays starting from 'start'
        
        # If no special subarray was found, return -1
        return min_length if min_length != float('inf') else -1

def minimumSubarrayLength(nums: List[int], k: int) -> int:
    return Solution().minimumSubarrayLength(nums, k)