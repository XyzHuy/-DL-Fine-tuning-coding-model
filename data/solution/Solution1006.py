import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def clumsy(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7
        
        # Start with the first part of the expression
        result = n * (n - 1) // (n - 2)
        n -= 3
        
        # Process the remaining numbers in chunks of 4
        while n >= 4:
            result += n - (n - 1) * (n - 2) // (n - 3)
            n -= 4
        
        # Handle the remaining numbers less than 4
        if n == 3:
            result += 3 - 2 * 1
        elif n == 2:
            result += 2 - 1
        elif n == 1:
            result += 1
        
        return result

def clumsy(n: int) -> int:
    return Solution().clumsy(n)