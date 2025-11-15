import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [v for i, v in enumerate(nums) if v != i + 1]

def findDuplicates(nums: List[int]) -> List[int]:
    return Solution().findDuplicates(nums)