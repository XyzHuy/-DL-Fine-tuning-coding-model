import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        # Iterate over all possible distributions of candies to the three children
        for i in range(min(n, limit) + 1):
            for j in range(min(n - i, limit) + 1):
                k = n - i - j
                if k <= limit:
                    count += 1
        return count

def distributeCandies(n: int, limit: int) -> int:
    return Solution().distributeCandies(n, limit)