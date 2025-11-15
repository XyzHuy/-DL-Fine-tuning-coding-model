import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target

def createTargetArray(nums: List[int], index: List[int]) -> List[int]:
    return Solution().createTargetArray(nums, index)