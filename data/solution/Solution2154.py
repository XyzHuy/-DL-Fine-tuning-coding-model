import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)  # Convert list to set for O(1) lookups
        while original in nums_set:
            original *= 2
        return original

def findFinalValue(nums: List[int], original: int) -> int:
    return Solution().findFinalValue(nums, original)