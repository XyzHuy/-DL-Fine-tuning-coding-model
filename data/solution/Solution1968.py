import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Sort the array to facilitate rearrangement
        nums.sort()
        
        # Create two halves of the sorted array
        mid = (len(nums) + 1) // 2
        left = nums[:mid]
        right = nums[mid:]
        
        # Interleave the two halves to ensure no element is the average of its neighbors
        result = []
        for i in range(len(left)):
            result.append(left[i])
            if i < len(right):
                result.append(right[i])
        
        return result

def rearrangeArray(nums: List[int]) -> List[int]:
    return Solution().rearrangeArray(nums)