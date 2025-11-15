import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # The maximum number of different types of candies Alice can eat is the minimum of
        # the number of unique candy types and half the total number of candies.
        return min(len(set(candyType)), len(candyType) // 2)

def distributeCandies(candyType: List[int]) -> int:
    return Solution().distributeCandies(candyType)