import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        
        # Function to calculate the greatest common divisor
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        
        # Function to calculate the least common multiple
        def lcm(x, y):
            return x * y // gcd(x, y)
        
        # Binary search for the nth magical number
        low, high = 1, n * min(a, b)
        lcm_ab = lcm(a, b)
        
        while low < high:
            mid = (low + high) // 2
            # Count how many magical numbers are <= mid
            count = mid // a + mid // b - mid // lcm_ab
            
            if count < n:
                low = mid + 1
            else:
                high = mid
        
        return low % MOD

def nthMagicalNumber(n: int, a: int, b: int) -> int:
    return Solution().nthMagicalNumber(n, a, b)