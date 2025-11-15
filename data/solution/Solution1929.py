import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

def getConcatenation(nums: List[int]) -> List[int]:
    return Solution().getConcatenation(nums)