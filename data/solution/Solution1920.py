import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]

def buildArray(nums: List[int]) -> List[int]:
    return Solution().buildArray(nums)