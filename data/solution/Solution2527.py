import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

def xorBeauty(nums: List[int]) -> int:
    return Solution().xorBeauty(nums)