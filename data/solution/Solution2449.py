import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort(key=lambda x: (x & 1, x))
        target.sort(key=lambda x: (x & 1, x))
        return sum(abs(a - b) for a, b in zip(nums, target)) // 4

def makeSimilar(nums: List[int], target: List[int]) -> int:
    return Solution().makeSimilar(nums, target)