import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count_less_or_equal(x: int) -> int:
            count = 0
            for i in range(1, m + 1):
                count += min(x // i, n)
            return count

        left, right = 1, m * n
        while left < right:
            mid = (left + right) // 2
            if count_less_or_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

def findKthNumber(m: int, n: int, k: int) -> int:
    return Solution().findKthNumber(m, n, k)