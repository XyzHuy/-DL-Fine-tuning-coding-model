import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        min_num = min(nums)
        n = len(nums)
        expected_set = set(range(min_num, min_num + n))
        return set(nums) == expected_set

def isConsecutive(nums: List[int]) -> bool:
    return Solution().isConsecutive(nums)