import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        count = 0
        n = len(hours)
        for i in range(n):
            for j in range(i + 1, n):
                if (hours[i] + hours[j]) % 24 == 0:
                    count += 1
        return count

def countCompleteDayPairs(hours: List[int]) -> int:
    return Solution().countCompleteDayPairs(hours)