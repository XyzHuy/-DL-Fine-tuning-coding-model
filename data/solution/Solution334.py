import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False

def increasingTriplet(nums: List[int]) -> bool:
    return Solution().increasingTriplet(nums)