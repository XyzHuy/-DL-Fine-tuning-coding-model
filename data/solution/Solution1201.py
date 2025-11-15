import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        from math import gcd
        
        # Function to calculate LCM using GCD
        def lcm(x, y):
            return x * y // gcd(x, y)
        
        # Function to count numbers <= num that are divisible by a, b, or c
        def count_ugly(num):
            count_a = num // a
            count_b = num // b
            count_c = num // c
            count_ab = num // lcm(a, b)
            count_ac = num // lcm(a, c)
            count_bc = num // lcm(b, c)
            count_abc = num // lcm(lcm(a, b), c)
            return count_a + count_b + count_c - count_ab - count_ac - count_bc + count_abc
        
        # Binary search for the nth ugly number
        low, high = 1, 2 * 10**9
        while low < high:
            mid = (low + high) // 2
            if count_ugly(mid) < n:
                low = mid + 1
            else:
                high = mid
        return low

def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
    return Solution().nthUglyNumber(n, a, b, c)