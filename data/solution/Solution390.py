import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def lastRemaining(self, n: int) -> int:
        remaining = n
        step = 1
        left_to_right = True
        head = 1
        
        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
            step *= 2
            remaining //= 2
            left_to_right = not left_to_right
        
        return head

def lastRemaining(n: int) -> int:
    return Solution().lastRemaining(n)