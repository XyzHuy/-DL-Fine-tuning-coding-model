import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of nums1 and nums2
        last = m + n - 1
        i, j = m - 1, n - 1
        
        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            else:
                nums1[last] = nums2[j]
                j -= 1
            last -= 1
        
        # If there are remaining elements in nums2
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    return Solution().merge(nums1, m, nums2, n)