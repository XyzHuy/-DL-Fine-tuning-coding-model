import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from itertools import pairwise
from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = Counter()
        ans = mx = 0
        for a, b in pairwise(nums):
            if a == key:
                cnt[b] += 1
                if mx < cnt[b]:
                    mx = cnt[b]
                    ans = b
        return ans

def mostFrequent(nums: List[int], key: int) -> int:
    return Solution().mostFrequent(nums, key)