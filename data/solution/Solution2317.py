import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result |= num
        return result

def maximumXOR(nums: List[int]) -> int:
    return Solution().maximumXOR(nums)