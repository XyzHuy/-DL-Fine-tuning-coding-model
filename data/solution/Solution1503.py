import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # Calculate the time the last ant on the left side falls off
        left_max_time = max(left) if left else 0
        # Calculate the time the last ant on the right side falls off
        right_max_time = n - min(right) if right else 0
        # The last moment when any ant falls off the plank
        return max(left_max_time, right_max_time)

def getLastMoment(n: int, left: List[int], right: List[int]) -> int:
    return Solution().getLastMoment(n, left, right)