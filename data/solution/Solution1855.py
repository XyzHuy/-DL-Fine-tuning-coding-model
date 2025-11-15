import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_distance = 0
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                max_distance = max(max_distance, j - i)
            else:
                i += 1
            j += 1
        
        return max_distance

def maxDistance(nums1: List[int], nums2: List[int]) -> int:
    return Solution().maxDistance(nums1, nums2)