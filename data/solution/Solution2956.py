import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        answer1 = sum(1 for num in nums1 if num in set2)
        answer2 = sum(1 for num in nums2 if num in set1)
        
        return [answer1, answer2]

def findIntersectionValues(nums1: List[int], nums2: List[int]) -> List[int]:
    return Solution().findIntersectionValues(nums1, nums2)