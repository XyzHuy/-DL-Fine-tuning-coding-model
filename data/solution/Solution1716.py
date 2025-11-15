import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        complete_weeks = n // 7
        remaining_days = n % 7
        
        # Calculate the total money for complete weeks
        for i in range(complete_weeks):
            total += sum(range(i + 1, i + 8))
        
        # Calculate the total money for the remaining days
        total += sum(range(complete_weeks + 1, complete_weeks + 1 + remaining_days))
        
        return total

def totalMoney(n: int) -> int:
    return Solution().totalMoney(n)