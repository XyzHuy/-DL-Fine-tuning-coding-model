import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = 0
        nums.sort()  # Sort the array to make it easier to find strong pairs
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                x, y = nums[i], nums[j]
                if abs(x - y) <= min(x, y):
                    max_xor = max(max_xor, x ^ y)
                else:
                    # Since the array is sorted, if the condition fails, no need to check further
                    break
        
        return max_xor

def maximumStrongPairXor(nums: List[int]) -> int:
    return Solution().maximumStrongPairXor(nums)