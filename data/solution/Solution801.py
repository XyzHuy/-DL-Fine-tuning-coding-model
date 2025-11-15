import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        keep = [0] * n
        swap = [0] * n
        
        # Base case
        keep[0] = 0
        swap[0] = 1
        
        for i in range(1, n):
            if nums1[i-1] < nums1[i] and nums2[i-1] < nums2[i]:
                if nums1[i-1] < nums2[i] and nums2[i-1] < nums1[i]:
                    keep[i] = min(keep[i-1], swap[i-1])
                    swap[i] = min(keep[i-1], swap[i-1]) + 1
                else:
                    keep[i] = keep[i-1]
                    swap[i] = swap[i-1] + 1
            else:
                keep[i] = swap[i-1]
                swap[i] = keep[i-1] + 1
        
        return min(keep[n-1], swap[n-1])

def minSwap(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minSwap(nums1, nums2)