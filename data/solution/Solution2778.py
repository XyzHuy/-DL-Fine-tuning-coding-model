import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        return sum(nums[i] * nums[i] for i in range(n) if (i + 1) % n == 0 or n % (i + 1) == 0)

def sumOfSquares(nums: List[int]) -> int:
    return Solution().sumOfSquares(nums)