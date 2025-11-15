import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(2, len(nums)):
            if (mx := max(mx, nums[i - 2])) > nums[i]:
                return False
        return True

def isIdealPermutation(nums: List[int]) -> bool:
    return Solution().isIdealPermutation(nums)