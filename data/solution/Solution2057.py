import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

def smallestEqual(nums: List[int]) -> int:
    return Solution().smallestEqual(nums)