import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        # Sort capacities in descending order to use the largest boxes first
        capacity.sort(reverse=True)
        
        used_capacity = 0
        for i, cap in enumerate(capacity):
            used_capacity += cap
            if used_capacity >= total_apples:
                return i + 1

def minimumBoxes(apple: List[int], capacity: List[int]) -> int:
    return Solution().minimumBoxes(apple, capacity)