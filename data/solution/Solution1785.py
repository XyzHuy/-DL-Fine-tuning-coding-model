import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        current_sum = sum(nums)
        difference = abs(goal - current_sum)
        return (difference + limit - 1) // limit

def minElements(nums: List[int], limit: int, goal: int) -> int:
    return Solution().minElements(nums, limit, goal)