import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        # Helper function to count the number of set bits in the binary representation of a number
        def countSetBits(n: int) -> int:
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        # Initialize the sum
        total_sum = 0
        
        # Iterate over the indices of nums
        for i in range(len(nums)):
            # Check if the number of set bits in the index is equal to k
            if countSetBits(i) == k:
                total_sum += nums[i]
        
        return total_sum

def sumIndicesWithKSetBits(nums: List[int], k: int) -> int:
    return Solution().sumIndicesWithKSetBits(nums, k)