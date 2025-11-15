import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        duplicate = sum(nums) - sum(num_set)
        missing = sum(range(1, n + 1)) - sum(num_set)
        return [duplicate, missing]

def findErrorNums(nums: List[int]) -> List[int]:
    return Solution().findErrorNums(nums)