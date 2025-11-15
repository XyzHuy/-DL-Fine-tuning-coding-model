import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return [i for i in range(1, 101) if (i in s1) + (i in s2) + (i in s3) > 1]

def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    return Solution().twoOutOfThree(nums1, nums2, nums3)