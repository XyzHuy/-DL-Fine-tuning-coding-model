import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # Convert lists to sets to find distinct elements and perform set operations
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find elements in nums1 that are not in nums2
        diff1 = list(set1 - set2)
        
        # Find elements in nums2 that are not in nums1
        diff2 = list(set2 - set1)
        
        return [diff1, diff2]

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    return Solution().findDifference(nums1, nums2)