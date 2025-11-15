import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        
        @lru_cache(None)
        def can_jump(position, jump_size):
            if position == stones[-1]:
                return True
            if position not in stone_set or jump_size <= 0:
                return False
            
            # Try jumping k-1, k, or k+1 units
            return (can_jump(position + jump_size - 1, jump_size - 1) or
                    can_jump(position + jump_size, jump_size) or
                    can_jump(position + jump_size + 1, jump_size + 1))
        
        # The first jump must be 1 unit
        return can_jump(1, 1) if 1 in stone_set else False

def canCross(stones: List[int]) -> bool:
    return Solution().canCross(stones)