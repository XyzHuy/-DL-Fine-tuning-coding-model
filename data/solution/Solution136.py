import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Using XOR to find the single number
        single = 0
        for num in nums:
            single ^= num
        return single

def singleNumber(nums: List[int]) -> int:
    return Solution().singleNumber(nums)