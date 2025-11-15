import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        
        return min_a * min_b

def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
    return Solution().maxCount(m, n, ops)