import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def trailing_zeroes(x: int) -> int:
            count = 0
            while x >= 5:
                x //= 5
                count += x
            return count
        
        # Binary search to find the smallest x such that trailing_zeroes(x) >= k
        left, right = 0, 5 * (k + 1)
        while left < right:
            mid = (left + right) // 2
            if trailing_zeroes(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        # Check if there is any x such that trailing_zeroes(x) == k
        if trailing_zeroes(left) == k:
            return 5
        else:
            return 0

def preimageSizeFZF(k: int) -> int:
    return Solution().preimageSizeFZF(k)