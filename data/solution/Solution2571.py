import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minOperations(self, n: int) -> int:
        operations = 0
        while n > 0:
            # Find the highest power of 2 less than or equal to n
            power = 1
            while power * 2 <= n:
                power *= 2
            
            # Check if it's better to subtract this power of 2 or add to the next power of 2
            if power * 2 - n < n - power:
                n = power * 2 - n
            else:
                n -= power
            
            operations += 1
        
        return operations

def minOperations(n: int) -> int:
    return Solution().minOperations(n)