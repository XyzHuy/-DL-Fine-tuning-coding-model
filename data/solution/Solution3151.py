import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True

def isArraySpecial(nums: List[int]) -> bool:
    return Solution().isArraySpecial(nums)