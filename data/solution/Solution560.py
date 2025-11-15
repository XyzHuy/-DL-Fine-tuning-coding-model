import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store the cumulative sum frequencies
        cumulative_sum_map = {0: 1}
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            # Check if there is a subarray (ending at the current index) which sums to k
            if (current_sum - k) in cumulative_sum_map:
                count += cumulative_sum_map[current_sum - k]
            
            # Update the cumulative sum map
            if current_sum in cumulative_sum_map:
                cumulative_sum_map[current_sum] += 1
            else:
                cumulative_sum_map[current_sum] = 1
        
        return count

def subarraySum(nums: List[int], k: int) -> int:
    return Solution().subarraySum(nums, k)