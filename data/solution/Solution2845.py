import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        # Dictionary to store the frequency of prefix sums modulo `modulo`
        prefix_count = defaultdict(int)
        # Initialize with prefix sum 0 having one count
        prefix_count[0] = 1
        
        current_count = 0
        result = 0
        
        for num in nums:
            # Update the current count based on the condition
            if num % modulo == k:
                current_count += 1
            
            # Calculate the required prefix sum to form an interesting subarray
            required_prefix = (current_count % modulo - k + modulo) % modulo
            
            # Add the number of valid previous prefixes to the result
            result += prefix_count[required_prefix]
            
            # Update the prefix count dictionary with the current prefix sum
            prefix_count[current_count % modulo] += 1
        
        return result

def countInterestingSubarrays(nums: List[int], modulo: int, k: int) -> int:
    return Solution().countInterestingSubarrays(nums, modulo, k)