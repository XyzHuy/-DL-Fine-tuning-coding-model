import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_cut_ribbons(length):
            count = 0
            for ribbon in ribbons:
                count += ribbon // length
            return count >= k
        
        left, right = 1, max(ribbons)
        result = 0
        while left <= right:
            mid = (left + right) // 2
            if can_cut_ribbons(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result

def maxLength(ribbons: List[int], k: int) -> int:
    return Solution().maxLength(ribbons, k)