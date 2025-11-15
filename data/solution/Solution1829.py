import random
import functools
import collections
import string
import math
import datetime


from functools import reduce
from operator import xor
from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        xs = reduce(xor, nums)
        for x in nums[::-1]:
            k = 0
            for i in range(maximumBit - 1, -1, -1):
                if (xs >> i & 1) == 0:
                    k |= 1 << i
            ans.append(k)
            xs ^= x
        return ans

def getMaximumXor(nums: List[int], maximumBit: int) -> List[int]:
    return Solution().getMaximumXor(nums, maximumBit)