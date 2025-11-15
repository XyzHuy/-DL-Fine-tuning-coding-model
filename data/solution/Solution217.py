import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set to track seen numbers
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

def containsDuplicate(nums: List[int]) -> bool:
    return Solution().containsDuplicate(nums)