import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        def max_subarray_sum_diff(arr1, arr2):
            max_diff = 0
            current_diff = 0
            for a, b in zip(arr1, arr2):
                current_diff = max(b - a, 0, current_diff + b - a)
                max_diff = max(max_diff, current_diff)
            return max_diff
        
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        
        max_diff_2_to_1 = max_subarray_sum_diff(nums1, nums2)
        max_diff_1_to_2 = max_subarray_sum_diff(nums2, nums1)
        
        potential_new_sum1 = sum1 + max_diff_2_to_1
        potential_new_sum2 = sum2 + max_diff_1_to_2
        
        return max(sum1, sum2, potential_new_sum1, potential_new_sum2)

def maximumsSplicedArray(nums1: List[int], nums2: List[int]) -> int:
    return Solution().maximumsSplicedArray(nums1, nums2)