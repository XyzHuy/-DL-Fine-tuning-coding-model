import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # Convert lists to sets to get unique elements
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Calculate the size of the intersection
        intersection = set1.intersection(set2)
        
        # Calculate the size of the unique elements in each set
        unique_in_set1 = len(set1) - len(intersection)
        unique_in_set2 = len(set2) - len(intersection)
        
        # Calculate the maximum possible size of the set s
        max_from_set1 = min(n // 2, unique_in_set1)
        max_from_set2 = min(n // 2, unique_in_set2)
        
        # The remaining spots can be filled by the intersection elements
        remaining_spots = (n // 2) - max_from_set1 + (n // 2) - max_from_set2
        intersection_elements_to_add = min(remaining_spots, len(intersection))
        
        # Total size of the set s
        max_set_size = max_from_set1 + max_from_set2 + intersection_elements_to_add
        
        return max_set_size

def maximumSetSize(nums1: List[int], nums2: List[int]) -> int:
    return Solution().maximumSetSize(nums1, nums2)