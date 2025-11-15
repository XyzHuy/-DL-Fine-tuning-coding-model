import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
        return running_sum

def runningSum(nums: List[int]) -> List[int]:
    return Solution().runningSum(nums)