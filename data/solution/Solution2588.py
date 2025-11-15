import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        # Dictionary to store the count of each prefix XOR value
        prefix_xor_count = defaultdict(int)
        prefix_xor_count[0] = 1  # Base case: a prefix XOR of 0 has occurred once (at the start)
        
        current_xor = 0
        beautiful_subarrays_count = 0
        
        for num in nums:
            current_xor ^= num  # Update the current prefix XOR
            # The number of times the current prefix XOR has occurred before
            beautiful_subarrays_count += prefix_xor_count[current_xor]
            # Increment the count of the current prefix XOR in the dictionary
            prefix_xor_count[current_xor] += 1
        
        return beautiful_subarrays_count

def beautifulSubarrays(nums: List[int]) -> int:
    return Solution().beautifulSubarrays(nums)