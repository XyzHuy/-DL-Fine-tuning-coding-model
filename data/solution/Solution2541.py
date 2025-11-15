import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if nums1 == nums2:
            return 0
        
        if k == 0:
            return -1
        
        increment_count = 0
        decrement_count = 0
        
        for a, b in zip(nums1, nums2):
            diff = a - b
            if diff % k != 0:
                return -1
            if diff > 0:
                decrement_count += diff // k
            elif diff < 0:
                increment_count += -diff // k
        
        if increment_count != decrement_count:
            return -1
        
        return increment_count

def minOperations(nums1: List[int], nums2: List[int], k: int) -> int:
    return Solution().minOperations(nums1, nums2, k)