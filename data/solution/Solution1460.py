import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # If both arrays have the same elements with the same frequency,
        # then one can be made equal to the other by reversing subarrays.
        return sorted(target) == sorted(arr)

def canBeEqual(target: List[int], arr: List[int]) -> bool:
    return Solution().canBeEqual(target, arr)