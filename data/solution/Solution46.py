import random
import functools
import collections
import string
import math
import datetime


from itertools import permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(p) for p in permutations(nums)]

def permute(nums: List[int]) -> List[List[int]]:
    return Solution().permute(nums)