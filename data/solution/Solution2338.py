import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from math import comb

MOD = 10**9 + 7

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        def prime_factors(x):
            factors = defaultdict(int)
            divisor = 2
            while x >= divisor * divisor:
                while (x % divisor) == 0:
                    factors[divisor] += 1
                    x //= divisor
                divisor += 1
            if x > 1:
                factors[x] += 1
            return factors
        
        def count_sequences(n, factors):
            total_ways = 1
            for count in factors.values():
                total_ways *= comb(n + count - 1, count)
                total_ways %= MOD
            return total_ways
        
        total_ideal_arrays = 0
        for value in range(1, maxValue + 1):
            factors = prime_factors(value)
            total_ideal_arrays += count_sequences(n, factors)
            total_ideal_arrays %= MOD
        
        return total_ideal_arrays

def idealArrays(n: int, maxValue: int) -> int:
    return Solution().idealArrays(n, maxValue)