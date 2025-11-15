import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_left

class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        def f(s):
            t = j = 0
            cnt = 0
            for i, x in enumerate(nums):
                t += x
                while t > s:
                    t -= nums[j]
                    j += 1
                cnt += i - j + 1
            return cnt >= k

        l, r = min(nums), sum(nums)
        return l + bisect_left(range(l, r + 1), True, key=f)

def kthSmallestSubarraySum(nums: List[int], k: int) -> int:
    return Solution().kthSmallestSubarraySum(nums, k)