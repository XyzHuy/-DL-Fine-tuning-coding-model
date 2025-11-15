import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # Convert lists to sets for faster lookup
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Check for common digits
        common_digits = set1.intersection(set2)
        if common_digits:
            return min(common_digits)
        
        # If no common digits, form the smallest possible two-digit number
        min1 = min(nums1)
        min2 = min(nums2)
        
        # Form the smaller number by placing the smaller digit first
        return min(min1, min2) * 10 + max(min1, min2)

def minNumber(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minNumber(nums1, nums2)