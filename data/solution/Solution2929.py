import random
import functools
import collections
import string
import math
import datetime


from math import comb

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n > 3 * limit:
            return 0
        ans = comb(n + 2, 2)
        if n > limit:
            ans -= 3 * comb(n - limit + 1, 2)
        if n - 2 >= 2 * limit:
            ans += 3 * comb(n - 2 * limit, 2)
        return ans

def distributeCandies(n: int, limit: int) -> int:
    return Solution().distributeCandies(n, limit)