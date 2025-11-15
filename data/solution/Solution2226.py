import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canDistribute(candies_per_child):
            count = 0
            for pile in candies:
                count += pile // candies_per_child
                if count >= k:
                    return True
            return False

        total_candies = sum(candies)
        if total_candies < k:
            return 0

        left, right = 1, max(candies)
        while left <= right:
            mid = (left + right) // 2
            if canDistribute(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right

def maximumCandies(candies: List[int], k: int) -> int:
    return Solution().maximumCandies(candies, k)