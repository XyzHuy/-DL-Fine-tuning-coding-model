import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return min(nums2) - min(nums1)

def addedInteger(nums1: List[int], nums2: List[int]) -> int:
    return Solution().addedInteger(nums1, nums2)