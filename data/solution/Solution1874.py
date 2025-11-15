import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Sort nums1 in ascending order
        nums1.sort()
        # Sort nums2 in descending order
        nums2.sort(reverse=True)
        
        # Compute the product sum
        product_sum = sum(a * b for a, b in zip(nums1, nums2))
        
        return product_sum

def minProductSum(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minProductSum(nums1, nums2)