import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        left, right = 0, sum(batteries) // n
        
        while left < right:
            mid = (left + right + 1) // 2
            total = 0
            for battery in batteries:
                total += min(battery, mid)
            if total // n >= mid:
                left = mid
            else:
                right = mid - 1
        
        return left

def maxRunTime(n: int, batteries: List[int]) -> int:
    return Solution().maxRunTime(n, batteries)