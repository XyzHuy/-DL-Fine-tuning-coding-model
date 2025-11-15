import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum(num - min_val for num in nums)

def minMoves(nums: List[int]) -> int:
    return Solution().minMoves(nums)