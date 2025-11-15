import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize the result
        result = 0
        
        # If nums2 is of odd length, XOR all elements of nums1
        if len(nums2) % 2 == 1:
            for num in nums1:
                result ^= num
        
        # If nums1 is of odd length, XOR all elements of nums2
        if len(nums1) % 2 == 1:
            for num in nums2:
                result ^= num
        
        return result

def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    return Solution().xorAllNums(nums1, nums2)