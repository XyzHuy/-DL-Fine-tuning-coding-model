import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_left

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def f(x: int) -> bool:
            return sum(v <= x for v in nums) > x

        return bisect_left(range(1, len(nums)), True, key=f) + 1

def findDuplicate(nums: List[int]) -> int:
    return Solution().findDuplicate(nums)