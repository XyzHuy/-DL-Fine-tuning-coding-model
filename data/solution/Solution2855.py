import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        i = 1
        while i < n and nums[i - 1] < nums[i]:
            i += 1
        if i == n:
            return 0  # The array is already sorted
        if i < n - 1 and nums[-1] > nums[0]:
            return -1  # More than one place where the order is broken, or the last element is greater than the first
        
        k = i + 1
        while k < n and nums[k - 1] < nums[k]:
            k += 1
        
        return -1 if k < n else n - i

def minimumRightShifts(nums: List[int]) -> int:
    return Solution().minimumRightShifts(nums)