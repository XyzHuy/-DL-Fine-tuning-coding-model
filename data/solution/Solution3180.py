import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import cache
from bisect import bisect_right

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        @cache
        def dfs(x: int) -> int:
            i = bisect_right(rewardValues, x)
            ans = 0
            for v in rewardValues[i:]:
                ans = max(ans, v + dfs(x + v))
            return ans

        rewardValues.sort()
        return dfs(0)

def maxTotalReward(rewardValues: List[int]) -> int:
    return Solution().maxTotalReward(rewardValues)