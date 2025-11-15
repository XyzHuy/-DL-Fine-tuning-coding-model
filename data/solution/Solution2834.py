import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        MOD = 10**9 + 7
        mid = target // 2

        if n <= mid:
            # We can use the first n natural numbers
            return (n * (n + 1) // 2) % MOD
        else:
            # Use numbers from 1 to mid, and then from target to (target + n - mid - 1)
            sum_first_part = mid * (mid + 1) // 2
            sum_second_part = (target + (target + n - mid - 1)) * (n - mid) // 2
            return (sum_first_part + sum_second_part) % MOD

def minimumPossibleSum(n: int, target: int) -> int:
    return Solution().minimumPossibleSum(n, target)