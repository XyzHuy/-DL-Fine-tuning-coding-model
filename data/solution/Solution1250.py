import random
import functools
import collections
import string
import math
import datetime


from math import gcd
from functools import reduce
from typing import List

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # Calculate the GCD of the entire array
        return reduce(gcd, nums) == 1

def isGoodArray(nums: List[int]) -> bool:
    return Solution().isGoodArray(nums)