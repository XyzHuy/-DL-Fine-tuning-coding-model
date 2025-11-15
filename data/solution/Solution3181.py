import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        nums = sorted(set(rewardValues))
        f = 1
        for v in nums:
            f |= (f & ((1 << v) - 1)) << v
        return f.bit_length() - 1

def maxTotalReward(rewardValues: List[int]) -> int:
    return Solution().maxTotalReward(rewardValues)