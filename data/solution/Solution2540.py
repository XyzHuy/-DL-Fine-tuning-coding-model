import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Use two pointers to find the smallest common element
        i, j = 0, 0
        
        # Traverse both arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        # If no common element is found, return -1
        return -1

def getCommon(nums1: List[int], nums2: List[int]) -> int:
    return Solution().getCommon(nums1, nums2)