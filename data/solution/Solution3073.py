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
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        right = [nums[-1]] * n
        for i in range(n - 2, -1, -1):
            right[i] = max(nums[i], right[i + 1])
        sl = SortedList([nums[0]])
        ans = 0
        for j in range(1, n - 1):
            if right[j + 1] > nums[j]:
                i = sl.bisect_left(nums[j]) - 1
                if i >= 0:
                    ans = max(ans, sl[i] - nums[j] + right[j + 1])
            sl.add(nums[j])
        return ans

def maximumTripletValue(nums: List[int]) -> int:
    return Solution().maximumTripletValue(nums)