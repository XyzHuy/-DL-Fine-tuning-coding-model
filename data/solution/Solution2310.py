import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        
        # If k is 0, we can only use multiples of 10, so num must be a multiple of 10
        if k == 0:
            return 1 if num % 10 == 0 else -1
        
        # Check for the smallest set size from 1 to 10
        for i in range(1, 11):
            if (i * k) % 10 == num % 10 and i * k <= num:
                return i
        
        return -1

def minimumNumbers(num: int, k: int) -> int:
    return Solution().minimumNumbers(num, k)