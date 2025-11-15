import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        # Determine the maximum number of bits needed to represent the largest number in nums
        max_bits = max(nums).bit_length()
        
        # Initialize the result to 0
        result = 0
        
        # Iterate over each bit position
        for bit in range(max_bits):
            count = 0
            
            # Count how many numbers have the current bit set to 1
            for num in nums:
                if (num >> bit) & 1:
                    count += 1
            
            # If at least k numbers have the current bit set to 1, set the bit in the result
            if count >= k:
                result |= (1 << bit)
        
        return result

def findKOr(nums: List[int], k: int) -> int:
    return Solution().findKOr(nums, k)