import random
import functools
import collections
import string
import math
import datetime


from typing import List
from itertools import permutations

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            
            for a, b, *rest in permutations(nums):
                for x in {a + b, a - b, a * b, (b and a / b)}:
                    if solve([x] + rest):
                        return True
            return False
        
        return solve(cards)

def judgePoint24(cards: List[int]) -> bool:
    return Solution().judgePoint24(cards)