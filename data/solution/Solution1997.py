import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nextVisit)
        days = [0] * n
        
        for i in range(n - 1):
            days[i + 1] = (2 * days[i] - days[nextVisit[i]] + 2) % MOD
        
        return days[-1]

def firstDayBeenInAllRooms(nextVisit: List[int]) -> int:
    return Solution().firstDayBeenInAllRooms(nextVisit)