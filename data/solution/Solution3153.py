import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter
from math import log10

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        n = len(nums)
        m = int(log10(nums[0])) + 1
        ans = 0
        for _ in range(m):
            cnt = Counter()
            new_nums = []
            for x in nums:
                x, y = divmod(x, 10)
                cnt[y] += 1
                new_nums.append(x)
            ans += sum(v * (n - v) for v in cnt.values()) // 2
            nums = new_nums
        return ans

def sumDigitDifferences(nums: List[int]) -> int:
    return Solution().sumDigitDifferences(nums)