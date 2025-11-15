import random
import functools
import collections
import string
import math
import datetime


from functools import cache
from typing import List
from math import inf

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        @cache
        def dfs(mask: int, pre: int) -> int:
            if mask == (1 << n) - 1:
                return abs(pre - nums[0])
            res = inf
            for cur in range(n):
                if mask >> cur & 1 == 0:
                    res = min(res, abs(pre - nums[cur]) + dfs(mask | (1 << cur), cur))
            return res

        def g(mask: int, pre: int):
            ans.append(pre)
            if mask == (1 << n) - 1:
                return
            res = dfs(mask, pre)
            for cur in range(n):
                if mask >> cur & 1 == 0:
                    if abs(pre - nums[cur]) + dfs(mask | (1 << cur), cur) == res:
                        g(mask | (1 << cur), cur)
                        break

        n = len(nums)
        ans = []
        g(1, 0)
        return ans

def findPermutation(nums: List[int]) -> List[int]:
    return Solution().findPermutation(nums)