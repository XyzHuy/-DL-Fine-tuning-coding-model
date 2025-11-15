import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        
        if primeFactors <= 3:
            return primeFactors
        
        # Number of 3's we can use
        quotient = primeFactors // 3
        remainder = primeFactors % 3
        
        if remainder == 0:
            return pow(3, quotient, MOD)
        elif remainder == 1:
            # Use one less 3 and replace it with 4 (2*2)
            return (pow(3, quotient - 1, MOD) * 4) % MOD
        else:
            # remainder == 2
            return (pow(3, quotient, MOD) * 2) % MOD

def maxNiceDivisors(primeFactors: int) -> int:
    return Solution().maxNiceDivisors(primeFactors)