import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Convert nums to a set to get unique elements
        unique_nums = set(nums)
        # Remove 0 if it exists in the set
        unique_nums.discard(0)
        # The number of operations is the size of the set
        return len(unique_nums)

def minimumOperations(nums: List[int]) -> int:
    return Solution().minimumOperations(nums)