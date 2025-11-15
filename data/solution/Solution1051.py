import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count += 1
        return count

def heightChecker(heights: List[int]) -> int:
    return Solution().heightChecker(heights)