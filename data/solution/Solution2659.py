import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from sortedcontainers import SortedList
from itertools import pairwise
from typing import List

class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        pos = {x: i for i, x in enumerate(nums)}
        nums.sort()
        sl = SortedList()
        ans = pos[nums[0]] + 1
        n = len(nums)
        for k, (a, b) in enumerate(pairwise(nums)):
            i, j = pos[a], pos[b]
            d = j - i - sl.bisect(j) + sl.bisect(i)
            ans += d + (n - k) * int(i > j)
            sl.add(i)
        return ans

def countOperationsToEmptyArray(nums: List[int]) -> int:
    return Solution().countOperationsToEmptyArray(nums)