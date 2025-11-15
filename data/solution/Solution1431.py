import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        return result

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    return Solution().kidsWithCandies(candies, extraCandies)