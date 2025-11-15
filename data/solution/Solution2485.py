import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def pivotInteger(self, n: int) -> int:
        total_sum = n * (n + 1) // 2
        left_sum = 0
        
        for x in range(1, n + 1):
            left_sum += x
            if left_sum == total_sum:
                return x
            total_sum -= x
        
        return -1

def pivotInteger(n: int) -> int:
    return Solution().pivotInteger(n)