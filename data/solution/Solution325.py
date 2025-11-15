import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # Dictionary to store the first occurrence of each prefix sum
        prefix_sum_indices = {0: -1}
        max_length = 0
        current_sum = 0
        
        for i, num in enumerate(nums):
            current_sum += num
            
            # Check if there is a prefix sum that, when subtracted from current_sum, equals k
            if (current_sum - k) in prefix_sum_indices:
                max_length = max(max_length, i - prefix_sum_indices[current_sum - k])
            
            # Store the first occurrence of the current_sum
            if current_sum not in prefix_sum_indices:
                prefix_sum_indices[current_sum] = i
        
        return max_length

def maxSubArrayLen(nums: List[int], k: int) -> int:
    return Solution().maxSubArrayLen(nums, k)