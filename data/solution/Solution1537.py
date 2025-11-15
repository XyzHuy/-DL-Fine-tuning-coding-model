import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        sum1, sum2 = 0, 0
        MOD = 10**9 + 7
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sum1 += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sum2 += nums2[j]
                j += 1
            else:
                # nums1[i] == nums2[j]
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
        
        # Add remaining elements of nums1
        while i < len(nums1):
            sum1 += nums1[i]
            i += 1
        
        # Add remaining elements of nums2
        while j < len(nums2):
            sum2 += nums2[j]
            j += 1
        
        return max(sum1, sum2) % MOD

def maxSum(nums1: List[int], nums2: List[int]) -> int:
    return Solution().maxSum(nums1, nums2)