import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        return math.gcd(min_num, max_num)

def findGCD(nums: List[int]) -> int:
    return Solution().findGCD(nums)