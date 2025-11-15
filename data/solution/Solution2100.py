import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if n < 2 * time + 1:
            return []
        
        # Arrays to store the number of consecutive non-increasing and non-decreasing days
        before = [0] * n
        after = [0] * n
        
        # Fill the before array
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                before[i] = before[i - 1] + 1
        
        # Fill the after array
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i + 1]:
                after[i] = after[i + 1] + 1
        
        # Collect all good days
        good_days = []
        for i in range(time, n - time):
            if before[i] >= time and after[i] >= time:
                good_days.append(i)
        
        return good_days

def goodDaysToRobBank(security: List[int], time: int) -> List[int]:
    return Solution().goodDaysToRobBank(security, time)