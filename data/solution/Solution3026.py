import random
import functools
import collections
import string
import math
import datetime


from typing import List
import collections

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store the minimum prefix sum up to the first occurrence of each number
        prefix_sum_map = collections.defaultdict(lambda: float('inf'))
        max_sum = float('-inf')
        current_prefix_sum = 0
        
        for num in nums:
            # Update the prefix sum map with the minimum prefix sum for the current number
            prefix_sum_map[num] = min(prefix_sum_map[num], current_prefix_sum)
            
            # Calculate the maximum sum for subarrays ending at the current index with difference k
            if (num + k) in prefix_sum_map:
                max_sum = max(max_sum, current_prefix_sum + num - prefix_sum_map[num + k])
            if (num - k) in prefix_sum_map:
                max_sum = max(max_sum, current_prefix_sum + num - prefix_sum_map[num - k])
            
            # Update the current prefix sum
            current_prefix_sum += num
        
        # If no good subarray is found, return 0
        return max_sum if max_sum != float('-inf') else 0

def maximumSubarraySum(nums: List[int], k: int) -> int:
    return Solution().maximumSubarraySum(nums, k)