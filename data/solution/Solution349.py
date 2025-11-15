import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to remove duplicates and allow for set operations
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of both sets
        intersection_set = set1.intersection(set2)
        
        # Convert the set back to a list and return
        return list(intersection_set)

def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return Solution().intersection(nums1, nums2)