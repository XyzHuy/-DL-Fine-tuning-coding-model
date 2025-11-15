import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]
        
        if start <= end:
            return list(range(start, end + 1))
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))

def mostVisited(n: int, rounds: List[int]) -> List[int]:
    return Solution().mostVisited(n, rounds)