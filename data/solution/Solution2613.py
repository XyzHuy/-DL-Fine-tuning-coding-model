import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def beautifulPair(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        min_value = float('inf')
        result = (0, 0)
        
        # To keep track of the coordinates when sorting
        indexed_nums1 = list(enumerate(nums1))
        indexed_nums2 = list(enumerate(nums2))
        
        # Sort both lists based on their values while keeping the original indices
        indexed_nums1.sort(key=lambda x: x[1])
        indexed_nums2.sort(key=lambda x: x[1])
        
        # Check the closest neighbors in the sorted lists
        for i in range(1, n):
            # Check for nums1 sorted order
            i1, val1 = indexed_nums1[i]
            j1, val1_prev = indexed_nums1[i - 1]
            current_value = abs(val1 - val1_prev) + abs(nums2[i1] - nums2[j1])
            if current_value < min_value:
                min_value = current_value
                result = (min(i1, j1), max(i1, j1))
            elif current_value == min_value:
                result = min(result, (min(i1, j1), max(i1, j1)))
            
            # Check for nums2 sorted order
            i2, val2 = indexed_nums2[i]
            j2, val2_prev = indexed_nums2[i - 1]
            current_value = abs(val2 - val2_prev) + abs(nums1[i2] - nums1[j2])
            if current_value < min_value:
                min_value = current_value
                result = (min(i2, j2), max(i2, j2))
            elif current_value == min_value:
                result = min(result, (min(i2, j2), max(i2, j2)))
        
        return list(result)

def beautifulPair(nums1: List[int], nums2: List[int]) -> List[int]:
    return Solution().beautifulPair(nums1, nums2)