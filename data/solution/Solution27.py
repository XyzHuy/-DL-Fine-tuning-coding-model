import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # This will be the count of elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

def removeElement(nums: List[int], val: int) -> int:
    return Solution().removeElement(nums, val)