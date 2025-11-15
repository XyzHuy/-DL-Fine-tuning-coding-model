import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in s]


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    return Solution().findDisappearedNumbers(nums)