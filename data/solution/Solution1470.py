import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [x for pair in zip(nums[:n], nums[n:]) for x in pair]

def shuffle(nums: List[int], n: int) -> List[int]:
    return Solution().shuffle(nums, n)